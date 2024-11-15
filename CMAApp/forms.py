from django import forms
from .models import JoinUs, Admin
from .models import Car, Product

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class JoinUsForm(forms.ModelForm):
    class Meta:
        model = JoinUs
        fields = ["fullname", "email", "username", "contact", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(),
            "confirm_password": forms.PasswordInput(),
        }
        labels = {
            "fullname": "Full Name",
            "email": "Email Address",
            "username": "Username",
            "contact": "Contact Number",
            "password": "Password",
            "confirm_password": "Confirm Password",
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match")

        return cleaned_data



#demo

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {"category":"Select Category"}

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
