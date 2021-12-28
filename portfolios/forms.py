
from django import forms

class BuySellForm(forms.Form):
    symbol = forms.CharField(label="Nhập mã và số lượng", max_length=10)
    shares = forms.IntegerField(label="", min_value=10)

    symbol.widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Mã CK'})
    shares.widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Số lượng'})
