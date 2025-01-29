from django.urls import path
from authen import views

urlpatterns=[
    path('',views.home, name='maison'),
    path('register',views.register,name='register'),
    path('login',views.logIn,name='login'),
    path('logout',views.logOut,name='logout'),
    path('activate/<uidb64>/<token>' , views.activate , name="activate")
   
    
    
]