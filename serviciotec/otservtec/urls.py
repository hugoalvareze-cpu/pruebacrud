from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('ot_list/', views.ot_list, name='ot_list'),
    path('inicio/', views.inicio, name='inicio'),
    path('ot_total/', views.ot_total, name='ot_total'),
    path('form_agregar_ot/', views.form_agregar_ot, name='form_agregar_ot'),
    path('form_modificar_ot/<int:pk>/', views.form_modificar_ot, name='form_modificar_ot'),
    path('lista_retiro_ot/', views.lista_retiro_ot, name='lista_retiro_ot'),
    path('form_modificar_retiro/<int:pk>/', views.form_modificar_retiro, name='form_modificar_retiro'),
    path('lista_cliente/', views.lista_cliente, name='lista_cliente'),
    path('form_agregar_cliente/', views.form_agregar_cliente, name='form_agregar_cliente'),
    path('form_modificar_cliente/<int:pk>/', views.form_modificar_cliente, name='form_modificar_cliente'),
    path('lista_zona/', views.lista_zona, name='lista_zona'),     
    path('form_agregar_zona/', views.form_agregar_zona, name='form_agregar_zona'),
    path('form_modificar_zona/<int:pk>/', views.form_modificar_zona, name='form_modificar_zona'),
    path('lista_equipo/', views.lista_equipo, name='lista_equipo'),
    path('form_agregar_equipo/', views.form_agregar_equipo, name='form_agregar_equipo'),
    path('form_modificar_equipo/<int:pk>/', views.form_modificar_equipo, name='form_modificar_equipo'),
    path('lista_bateria/', views.lista_bateria, name='lista_bateria'),
    path('form_agregar_bateria/', views.form_agregar_bateria, name='form_agregar_bateria'),
    path('form_modificar_bateria/<int:pk>/', views.form_modificar_bateria, name='form_modificar_bateria'),         
    path('lista_tecnicos/', views.lista_tecnicos, name='lista_tecnicos'), 
    path('vista_form_ot/<int:pk>/', views.vista_form_ot, name='vista_form_ot'),              
]

