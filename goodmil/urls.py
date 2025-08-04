from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, BlogSitemap, ProjectSitemap, PropertySitemap

admin.site.site_header = 'GOODMILL CONSTRUCTION TEA ADMIN'
admin.site.site_title = 'GOODMILL CONSTRUCTION ADMIN PANEL'
admin.site.index_title = 'WELCOME TO GOODMILL CONSTRUCTION ADMIN PANEL'

sitemaps = {
    'static': StaticSitemap,
    'blogs': BlogSitemap,
    'projects': ProjectSitemap,
    'properties': PropertySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


