from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
#from core.views import index,contact

from .forms import LoginForm # to specify the login_form we created on forms.py

app_name = 'core'


urlpatterns = [
    path('',views.index, name= 'index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form = LoginForm), name='login'),
    #unlike traditional method where we define the .html file on views we are defining here 
]
