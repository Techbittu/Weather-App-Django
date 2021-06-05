from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='home'),
    path("register", views.register_request, name="register"),
    path('delete/<city_name>/',views.delete_city, name='delete_city'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]