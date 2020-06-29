from django.urls import path
from .views import CEOView, CEODetailView
from django.views.generic.base import TemplateView
from .views import BlogView




urlpatterns = [
    path('', CEOView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', TemplateView.as_view(template_name='landing/about.html'), name='about'),
    path('<int:pk>/', CEODetailView.as_view(), name='detail'),
    path('contact/', TemplateView.as_view(template_name='landing/contact.html'), name='contact')
]
