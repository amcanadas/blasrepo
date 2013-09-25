from django.views.generic import ListView,DetailView
from programacion.models import Programacion

class ProgramacionList(ListView):
    model = Programacion

class ProgramacionDetail(DetailView):
    model = Programacion

    def get_context_data(self, **kwargs):
        context = super(ProgramacionDetail, self).get_context_data(**kwargs)
        context['pesosOA'] = self.object.pesoraenmateria_set.all()
        return context