from django import forms

from ordersapp.models import Order
from productsapp.models import TechnicalSolutionsHasService
from servicesapp.models import Service


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service']

    def __init__(self, *args, **kwargs):
        qs = []
        if 'queryset' in kwargs and kwargs['queryset'] is not None:
            queryset = kwargs.pop('queryset')
            qs = Service.objects.filter(technicalsolutionshasservice__technicalsolutions_id=queryset).order_by('name')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = qs
