from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('negocio/create', views.NegocioCreate.as_view(), name="negocio_create"),
    path('categoria/01/', views.Categoria1List.as_view(), name="categoria1"),
    path('categoria/02/', views.Categoria2List.as_view(), name="categoria2"),
]