from django.urls import path

from . import views

urlpatterns=[
    path("",views.home,name="login"),
    path("signup/",views.signupForm,name='signup'),
    path("details/",views.details,name='details'),
    path("logout/",views.user_logout,name='logout'),
    path("set_password/",views.setuserpassword,name='set_password'),
    path("change_password/",views.changeuserpassword,name='change_password'),
]