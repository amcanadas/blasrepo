from django.views.generic import ListView,DetailView
from programacion.models import Programacion

class ProgramacionList(ListView):
    model = Programacion