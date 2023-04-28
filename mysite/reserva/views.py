#from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("Reservacion de Hoteles")

from django.shortcuts import render
from .models import Reserva

def reserva_all(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'reserva_all.html', context)