from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .models import CEO, Blog
from .forms import BlogForm


class CEOView(ListView):
    model = CEO
    template_name = 'landing/index.html'
    paginate_by = 2

class CEODetailView(DetailView):
    model = CEO
    template_name = 'landing/detail.html'
    context_object_name = "ceo"

class BlogView(SuccessMessageMixin, CreateView, ListView):
    model = Blog
    template_name = 'landing/blog.html'
    form_class = BlogForm
    success_url = '/'
    success_message = "Ваше сообщение отправлено!"
