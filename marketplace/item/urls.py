from django.urls import path

from . import views   #to get all the views.py(item) content

app_name = 'item' #name space for this app

urlpatterns = [
    path('<int:pk>/', views.detail, name = 'detail'),
    path('new', views.new, name = 'new'),
]

"""<int:pk>/ when this has an integer primarykey we want to use views.detail

"""

 