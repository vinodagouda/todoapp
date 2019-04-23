from django import forms
from .models import ToDoDetails

class ToDoCreateForm(forms.ModelForm):
    
    class Meta:
        model = ToDoDetails
        fields = [ 'title', 'description', 'user' ]
#        exclude = ('user', )

        widgets = {
#            'title': forms.CharField(attrs={'placeholder': 'Add To Do Title'}),
#            'description': forms.Textarea(attrs={'placeholder': 'Add To Do description'}),
            'user': forms.HiddenInput()
        }
    
"""class ProductBasicForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'title', 'upc', 'description', 'store', 'structure', 'productCategories', 'createdby', \
                'vendor', 'rating', 'has_price_plan']
        widgets = {
            'title' : forms.TextInput(attrs={'autocomplete': 'off'}),
            'productCategories' : M2MSelect(),
            'createdby' : forms.HiddenInput(),
            'vendor' : forms.HiddenInput(),
            'rating' : forms.HiddenInput(),
            'store' : forms.HiddenInput(),
            'structure' : forms.HiddenInput(),
            'has_price_plan': forms.HiddenInput(),"""
            #'productFilterOptions' : M2MSelect(attrs={'multiple':'multiple', 'required' : 'false'}),}