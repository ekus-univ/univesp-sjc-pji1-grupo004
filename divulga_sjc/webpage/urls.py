from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('negocio/create', views.NegocioCreate.as_view(), name="negocio_create")
]