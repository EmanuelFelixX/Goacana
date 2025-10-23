"""
URL configuration for Goacana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('perfil/', perfil, name='perfil'),
    path('cardapio/', cardapio, name = 'cardapio'),
    path('admins/', admins, name= 'admins'),
    path('editordecadarpio/', editordecadarpio, name='editordecadarpio'),
    path('login/', login, name='login'),
    path('publicacao/', publicacao, name='publicacao'),
    path('add_prato/', add_prato, name='add_prato'),
    path('edit_prato/<int:id>/', edit_prato, name='edit_prato'),
    path('rem_prato/<int:id>/', rem_prato, name='rem_prato'),
    path('disp_prato/<int:id>/', diponibilidade_prato, name='disp_prato'),
    path('rem_cat/<int:id>/', rem_cat, name='rem_cat'),
    path('rem_acomp/<int:id>/', rem_acomp, name='rem_acomp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)