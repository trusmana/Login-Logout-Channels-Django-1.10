from django.forms import ModelForm
from django import forms
from .models import Order, Product
OPTIONS = (
    ('Postpay','Postpay'),
    ('Prepay (Full)','Prepay (Full)'),
    ('Prepay (Half)', 'Prepay (Half)')
)
OPTIONS2 = (
    ('Confirm', 'Confirm'),
    ('Ready', 'Ready'),
    ('Send', 'Send'),
    ('Delivered', 'Delivered'),
    ('Returned', 'Returned'),
    ('Cancelled', 'Cancelled')
)

class OrderForm(ModelForm):
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    qt = forms.IntegerField(initial=1)### Quantity

    class Meta:
        model = Order
        fields = ['name','telepon','Alamat','delivery_date','product_id','payment_option','qt','order_status']

class ProdukForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_details','harga']
