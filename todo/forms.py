# forms.py

from django import forms

class EmployeeForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    latitude = forms.CharField(label='Latitude', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.CharField(label='Longitude', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    employee_id = forms.CharField(label='Employee ID', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label='Country', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
