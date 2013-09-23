# -*- coding: utf-8 -*-
from django.views.generic import ListView,DetailView
from normativa.models import Materia

class MateriaList(ListView):
    model = Materia

class MateriaDetail(DetailView):
    model = Materia

    def get_context_data(self, **kwargs):
        context = super(MateriaDetail, self).get_context_data(**kwargs)
        context['contenidos'] = self.object.contenido_set.all()
        context['resultados'] = self.object.resultadoaprendizaje_set.all()
        return context
