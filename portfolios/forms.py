
from django import forms
from .models import Transaction
from django.db.models import Count, Sum, Min, Max


CHOICES = list(Transaction.objects.all() \
            .values('symbol').annotate(company=Max('company')).order_by('-company') \
            .values_list('symbol', 'company'))

from portfolios.models import Transaction

# tuple(Transaction.objects.values_list('symbol', 'company')) #worked

class BuyForm(forms.Form):
    symbol = forms.CharField(label="", max_length=10)
    shares = forms.IntegerField(label="", min_value=10)

    symbol.widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Mã CK'})
    shares.widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Số lượng'})


# không dùng
class SellForm(forms.Form):
    # symbol = forms.CharField(label="Nhập mã và số lượng", max_length=10)
    symbol = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    shares = forms.IntegerField(label="", min_value=10)

    symbol.widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Mã CK'})
    shares.widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Số lượng'})
