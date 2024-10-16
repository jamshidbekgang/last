from django import forms
from .models import MyUser, Product, Category, ProductImages



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']  

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    def __init__(self, *a, **b) -> None:
        super().__init__(*a, **b)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class': 'form-control'})



class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'name', 'description', 'price', 'category', 'tags'}
    def __init__(self, *a, **b) -> None:
        super().__init__(*a, **b)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class': 'form-control'})


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password', 'photo', 'first_name', 'last_name']
    def __init__(self, *a, **b) -> None:
        super().__init__(*a, **b)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class': 'form-control'})
        
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *a, **b) -> None:
        super().__init__(*a, **b)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class': 'form-control'})

class EditForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','description','price','category', 'tags', 'rasm']  
               

class ProductImagesForm(forms.ModelForm):
	class Meta:
		model = ProductImages
		fields = ['image']         
     