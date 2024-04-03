
from django.urls import path
from todo import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category_list/',views.category_list, name='category_list'),
    path('category-service-list/<int:cat_id>',views.category_service_list,name='category-service-list'),
    path('contact/',views.contact,name='contact'),
   

    
]
