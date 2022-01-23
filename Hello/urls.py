"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include2('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "RoySpace"
admin.site.site_title = "RoySpace Admin Portal"
admin.site.index_title = "Welcome to RoySpace"

urlpatterns = [
    path('admin/', admin.site.urls),  #Write '/admin' after port num in server then send to admin page 
    path('', include('home.urls'))   #' ' -> means write some then send into home page here its home app
]