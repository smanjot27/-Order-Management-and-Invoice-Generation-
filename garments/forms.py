from django import forms
from django.core.exceptions import ValidationError
from garments.models import Order, tailor
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        exclude=['order_id','order_received']
        widgets={"amount" :forms.TextInput(attrs={'placeholder' : 'Amount'}) , "advance" : forms.TextInput(attrs={'placeholder' : 'Advance'}), "mobile_number": forms.TextInput(attrs={'placeholder' : 'Mobile Number'}), "delivery_date": forms.DateInput(attrs={'placeholder' : 'YYYY-MM-DD'}), "order_name" : forms.TextInput(attrs={'placeholder' : 'Order Name'}), "tailor_assigned" :forms.TextInput(attrs={'placeholder' : "Tailor Assigned"}), "salesman_assigned" : forms.TextInput(attrs={'placeholder' : "Salesman Assigned"}), 'serial_number' : forms.TextInput(attrs={'placeholder' : 'Serial Number'})}
       # error_messages={ 'mobile_number' : { 'invalid':_('Enter a valid 10 digit Mobile Number') },}
    def clean_mobile_number(self):
        mobile = self.cleaned_data['mobile_number']
        if len(mobile)!=10:
            raise ValidationError("Enter a Valid 10 digit Mobile Number")
        return mobile

class tailors(forms.ModelForm):
    class Meta:
        model=tailor
        exclude=['tailorid']
        widgets={"tailor_name" :forms.TextInput(attrs={'placeholder' : 'Tailor Name'})}
