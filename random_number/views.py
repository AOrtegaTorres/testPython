from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Number

class NumberList(ListView):
    model = Number

class NumberDetail(DetailView):
    model = Number

class NumberUpdate(UpdateView):
    model = Number
    success_url = reverse_lazy('numbers:list')
    fields = ['number', 'created']


class NumberDelete(DeleteView):
    model = Number
    success_url = reverse_lazy('numbers:list')

def save(request):
    instance = Number()
    instance.number = request.POST['one']
    instance.save()
      
    return HttpResponseRedirect('/')
