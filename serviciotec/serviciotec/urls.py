from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('otservtec.urls')),  # conecta las rutas de tu app
]
