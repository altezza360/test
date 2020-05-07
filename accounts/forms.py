from django import forms
from django.forms import ModelForm
from .models import Specialist, Order, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SpecialistForm(ModelForm):
    class Meta:
        model = Specialist
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['description', 'price', 'specialist', 'status']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']