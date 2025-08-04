from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from home.models import Blog, Project, Propertie

class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'blog', 'contact-us', 'gallery', 'projects', 'realestate', 'services', 'apply']
    
    
    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/blog-post/{obj.slug}'
    
class ProjectSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/project-page/{obj.slug}'
    
class PropertySitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Propertie.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/realestate-page/{obj.slug}'