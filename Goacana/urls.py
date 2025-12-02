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
    path('cardv2', cardv2, name='cardv2'),
    path('admins/', admins, name= 'admins'),
    path('editordecadarpio/', editordecadarpio, name='editordecadarpio'),
    path('login/', logins, name='login'),
    path('publiview/<int:id>/', publiview, name='publiview'),
    path('lista_publi/', lista_publi, name='lista_publi'),
    path('publicacao/', publicacao, name='publicacao'),
    path('edit_publi/<int:id>/', edit_publi, name='edit_publi'),
    path('rem_publi/<int:id>/', rem_publi, name='rem_publi'),
    path('add_prato/', add_prato, name='add_prato'),
    path('edit_prato/<int:id>/', edit_prato, name='edit_prato'),
    path('edit_cat/<int:id>/', edit_cat, name='edit_cat'),
    path('rem_prato/<int:id>/', rem_prato, name='rem_prato'),
    path('disp_prato/<int:id>/', diponibilidade_prato, name='disp_prato'),
    path('dest_prato/<int:id>/', destaque_prato, name='dest_prato'),
    path('rem_cat/<int:id>/', rem_cat, name='rem_cat'),
    path('rem_acomp/<int:id>/', rem_acomp, name='rem_acomp'),
    path('rem_img/<int:id>/', rem_img, name='rem_img'),
    path('users/', lista_users, name='users'),
    path('cad_user/', cad_user, name='cad_user'),
    path('edit_user/<int:id>/', edit_user, name='edit_user'),
    path('chn/<int:id>', edit_password, name='chn'),
    path('logoff/', logoff, name='logoff'),
    #path('envia_email/', send_my_email, name='envia_email'), apenas ativar no computador final
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)