from django.urls import path

from . import views   #to get all the views.py(item) content

app_name = 'item' #name space for this app

urlpatterns = [
    path('<int:pk>/', views.detail, name = 'detail'),
    
    path('new/', views.new, name = 'new'),
    
    path('<int:pk>/edit', views.edit, name = 'edit'),
    
    path('<int:pk>/delete', views.delete, name = 'delete'),
    
    
    
    #path('', views.items, name='items'),
]

"""<int:pk>/ when this has an integer primarykey we want to use views.detail
Alathough  path('<int:pk>/', views.detail, name = 'detail'), was created and implemented before      path('new/', views.new, name = 'new'),
we had a problem when we placed path('new/', views.new, name = 'new'), under path('<int:pk>/', views.detail, name = 'detail'),

Therefore, we had to place     path('new/', views.new, name = 'new'), before     path('<int:pk>/', views.detail, name = 'detail'),


"""

 