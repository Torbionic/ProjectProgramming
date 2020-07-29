from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['blog', 'about']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()



