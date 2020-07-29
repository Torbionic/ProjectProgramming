from django.urls import path
from .views import CEOView, CEODetailView
from django.views.generic.base import TemplateView
from .views import BlogView, BlogUpdate, BlogDelete
from .sitemaps import StaticViewSitemap, BlogSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}


urlpatterns = [
    path('', CEOView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('<int:pk>/update/', BlogUpdate.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDelete.as_view(), name='blog_delete'),
    path('about/', TemplateView.as_view(template_name='landing/about.html'), name='about'),
    path('<int:pk>/', CEODetailView.as_view(), name='detail'),
    path('contact/', TemplateView.as_view(template_name='landing/contact.html'), name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]
