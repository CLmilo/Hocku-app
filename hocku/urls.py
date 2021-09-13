"""hocku URL Configuration

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
#from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hocku.view import login
from Apps.GestionPersonas import views
#from Apps.GestionPersonas.views import  Login
#from Apps.GestionPersonas import urls as Personas_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', PersonasView.as_view()),
    #path('index/', include(Personas_urls.urlpatterns)),
   # path('login/', views.login),
    #path('login/', login),
    path('', include('R_Grados.urls')),
    path('', include('Apps.GestionPersonas.urls')),
    #path('buscar/',buscar),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

