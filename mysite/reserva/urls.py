#from django.urls import path

#from . import views

##urlpatterns = [
 #   path("", views.index, name="index"),
#]

from django.urls import path
from .views import reserva_all

urlpatterns = [
    path('all/', reserva_all, name='reserva_all'),
    # otras rutas
]
