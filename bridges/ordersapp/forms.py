from django import forms
from productsapp.models import TechnicalSolutionsHasService


class OrderForm(forms.ModelForm):
    class Meta:
        model = TechnicalSolutionsHasService
        fields = ['service']

    def __init__(self, *args, **kwargs):
        qs = []
        if 'product' in kwargs and kwargs['product'] is not None:
            product = kwargs.pop('product')
            qs = TechnicalSolutionsHasService.objects.filter(technicalsolutions_id=product).order_by('service')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = qs