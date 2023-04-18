"""puddle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #for items path


#to handle media files locally

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('core.urls')),
    
    path('admin/', admin.site.urls),

    path('items/', include('item.urls')),  #this points to the urls.py we created in item all urls that start with item will automatically
                                            #refer to urls,py(item) andif there is a path with primary key there"""
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


