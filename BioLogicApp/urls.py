from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 importante: con namespace
    path('', include('empleados.urls')),
]