from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),


    path('<int:contact/contact_id>/', views.contact, name='contact'),
    path('<contact/create/', views.contact, name='contact'),
    path('<int:contact/contact_id>/update/', views.contact, name='contact'),
    path('<int:contact/contact_id>/delete/', views.contact, name='contact'),
]
