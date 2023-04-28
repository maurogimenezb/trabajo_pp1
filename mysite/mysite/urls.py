from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    
    path("reserva/", include("reserva.urls")),
    path("admin/", admin.site.urls),
]