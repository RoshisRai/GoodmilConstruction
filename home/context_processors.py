from .models import Blog

def footer_blogs(request):
    blog = Blog.objects.all().order_by('-id')[:2]
    context = {
        'footer_blogs': blog
    }
    return context

from django.conf import settings

def site(request):
    return {'SITE_URL': settings.SITE_URL}