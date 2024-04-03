from django.shortcuts import render
import requests
from .forms import EmployeeForm

from django.http import HttpResponseRedirect
import requests
from . models import *

def employee_list(request):
    api_url = "https://api.findofficers.com/hiring_test/get_all_employee"
    response = requests.get(api_url)
    employees = response.json()  
    return render(request, 'employee_list.html', {'employees': employees})


def get_employees(request):
    api_url = 'https://api.findofficers.com/hiring_test/get_all_employee'
    response = requests.get(api_url)

    if response.status_code == 200:
        employees = response.json()
    else:
        employees = []  # Handle API errors gracefully

    return render(request, 'map.html', {'employees': employees})


# views.py




# # def add_employee(request):
# #     if request.method == 'POST':
# #         form = EmployeeForm(request.POST)
# #         if form.is_valid():
# #             data = {
# #                 'firstName': form.cleaned_data['first_name'],
# #                 'lastName': form.cleaned_data['last_name'],
# #                 'email': form.cleaned_data['email'],
# #                 'phoneNumber': form.cleaned_data['phone_number'],
# #                 'latitude': form.cleaned_data['latitude'],
# #                 'longitude': form.cleaned_data['longitude'],
# #                 'employeeID': form.cleaned_data['employee_id'],
# #                 'city': form.cleaned_data['city'],
# #                 'country': form.cleaned_data['country']
# #             }
# #             response = requests.post('https://api.findofficers.com/hiring_test/add_employee', json=data)
# #             if response.status_code == 200:
# #                 return render(request, 'success.html')
# #             else:
# #                 return render(request, 'error.html')
# #     else:
# #         form = EmployeeForm()
# #     return render(request, 'add_employee.html', {'form': form})

# # views.py



# def add_employee(request):
#     if request.method == 'POST':
#         # Extract data from the POST request
#         first_name = request.POST.get('firstName')
#         last_name = request.POST.get('lastName')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phoneNumber')
#         latitude = request.POST.get('latitude')
#         longitude = request.POST.get('longitude')
#         employee_id = request.POST.get('employeeID')
#         city = request.POST.get('city')
#         country = request.POST.get('country')

#         # Prepare data for the API request
#         data = {
#             'firstName': first_name,
#             'lastName': last_name,
#             'email': email,
#             'phoneNumber': phone_number,
#             'latitude': latitude,
#             'longitude': longitude,
#             'employeeID': employee_id,
#             'city': city,
#             'country': country
#         }

#         # Send POST request to the API endpoint
#         response = requests.post('https://api.findofficers.com/hiring_test/add_employee', json=data)
        
#         # Check if the request was successful
#         if response.ok:
#             # Redirect to a success page or render a success template
#             return render(request, 'success.html')
#         else:
#             # If the request failed, render an error template or redirect to an error page
#             return render(request, 'error.html')
#     else:
#         # If it's not a POST request, render the form template
#         return render(request, 'add_employee.html')


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'categories.html',{'data':data})

# Product List According to Category
def category_service_list(request, cat_id):
    additional_services = [
        {'title': 'Shampoo seats and carpets', 'price': 59},
        {'title': 'Shampoo only seats', 'price': 29},
        {'title': 'Pet hair removal', 'price': 25},
        {'title': 'Engine cleaning', 'price': 45},
        {'title': 'Clay bar', 'price': 20},
        {'title': 'Waxing', 'price': 45},
        {'title': 'Buffing', 'price': 145},
        {'title': 'Polish (Sedan)', 'price': 180},
        {'title': 'Polish (SUV)', 'price': 235},
        {'title': 'Polish (Truck)', 'price': 265},
    ]
    category = Category.objects.get(id=cat_id)
    data = CarService.objects.filter(categories=category).order_by('-id')

    return render(request, 'services_list.html', {'data': data, 'additional_services': additional_services})

