from django.urls import path
from .views import *

urlpatterns = [
   # path('', AuthLoginView.as_view(), name="auth_login"),
    path('', PersonasView.as_view(), name="index"),
]
