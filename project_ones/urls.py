"""project_ones URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from homepage import views as hp_views
from password_generator import views as pg_views
from portfolio import views as pt_views

urlpatterns = [
    path('', hp_views.home, name='home'), #首頁
    path('about/', hp_views.about, name='about'),
    path('password_generator/', pg_views.generator, name='password_generator'), #密碼生成器
    path('password/', pg_views.password, name='password'), 
    path('admin/', admin.site.urls, name='admin'), #後台
    path('portfolio/', pt_views.info, name='portfolio'), #自傳
    path('blog/', include('blog.urls'), name='blog'), #日記
    
    

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
