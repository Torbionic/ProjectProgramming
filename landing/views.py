from django.shortcuts import render
from django.views.generic import ListView

from .models import CEO


class CEOView(ListView):
    model = CEO
    template_name = 'landing/index.html'

