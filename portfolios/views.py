from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
import decimal

from .models import Transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum

from .helpers import lookup, apology, usd
from .forms import BuySellForm



def index(request):
    return render(request, 'portfolios/index.html')

@login_required
def my_portfolio(request):
    current_user = request.user
    
    # stocks = db.execute("SELECT symbol, name, price, sum(shares) as total_shares\
    #     from transactions\
    #     WHERE user_id = ? GROUP BY user_id, symbol, name", user_id)
    stocks = Transaction.objects.filter(client=current_user, status='pending') \
        .values('symbol', 'company') \
        .annotate(total_shares = Sum('shares')) \
        .order_by('symbol')
    print(stocks)
    # chua confirm
    cash = current_user.profile.cash

    # Use lookup API to get the current price for each stock
    stocks = [dict(x, **{'price': lookup(x['symbol'])['price']}) for x in stocks]

    stocks = [dict(x, **{'total': x['price']*x['total_shares']}) for x in stocks]

    sum_totals = cash + sum([decimal.Decimal(x['total']) for x in stocks])

    
    return render(request, 'portfolios/my_portfolio.html', {'stocks':stocks, 'cash': usd(cash), 'sum_total': usd(sum_totals), 'lookup': lookup, 'usd': usd})

# def quote(request):
#     return render(request, 'portfolios/quote.html', 
#                 {'section': 'quote'})

@login_required
def sell(request):
    form = BuySellForm()
    return render(request, 'portfolios/sell.html', 
                    {'form': form})

@login_required
def buy(request):
    if request.method == 'POST':
        form = BuySellForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            symbol = cd['symbol'].upper()
            shares = int(cd['shares'])
            item = lookup(symbol)
            
            if not item:
                return apology(request, "INVALID SYMBOL", 400)
            
            current_user = request.user    
            
            cash = current_user.profile.cash
            print(f'\n\n{cash}\n\n')
            
            item_name = item['name']
            item_price = item['price']
            total_price = item_price * shares
            if cash < total_price:
                return apology(request, "not enough cash")
            
            current_cash = cash - decimal.Decimal(total_price)
            # # chú ý, nếu k đc cả 2 thì rollback 
    
            transactions = Transaction(client=current_user, company=item_name, shares=shares, price=item_price, action='buy', symbol=symbol)
            transactions.save()
            
            current_user.profile.cash = current_cash
            current_user.save()
            
            messages.success(request, 'You have successfully bought shares!')
            return redirect('portfolios:index')
    else:
        form = BuySellForm()
        return render(request, 'portfolios/buy.html', {'form': form})

    

   
def history(request):
    transactions = Transaction.objects.all().values()
    transactions = [dict(x, **{'price': usd(x['price'])}) for x in transactions]
    return render(request, 'portfolios/history.html', {'transactions': transactions})
