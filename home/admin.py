from django.contrib import admin
from .models import Blog, GalleryCategorie, Gallery, ProjectCategorie, Project, Propertie, PropertyAgent, PropertyLocation, PropertyEnquirie, ContactUs, NewsletterSubscriber, ApplyNow
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    search_fields = ['title__contains', 'author__contains']

    class Media:
        js = ('js/tinyinject.js',)

@admin.register(GalleryCategorie)
class GalleryCategorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name__contains']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location', 'created_at', 'updated_at']
    search_fields = ['title__contains', 'location__contains']

@admin.register(ProjectCategorie)
class ProjectCategorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name__contains']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'title', 'location', 'created_at', 'updated_at']
    search_fields = ['title__contains','client__contains', 'location__contains']

    class Media:
        js = ('js/tinyinject.js',)

@admin.register(PropertyAgent)
class PropertyAgentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone','properties', 'created_at', 'updated_at']
    search_fields = ['name__contains', 'email__contains', 'phone__contains']

    def properties(self, obj):
        property_list = []
        properties = Propertie.objects.filter(agent=obj)
        property_list.append(properties.count())
        for i in properties:
            property_list.append(i)
        return property_list

@admin.register(Propertie)
class PropertieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title__contains']

    class Media:
        js = ('js/tinyinject.js',)

@admin.register(PropertyLocation)
class PropertyLocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name__contains']

@admin.register(PropertyEnquirie)
class PropertyEnquirieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone','property', 'created_at', 'updated_at']
    search_fields = ['name__contains', 'email__contains', 'phone__contains']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'subject', 'preference', 'created_at', 'updated_at']
    search_fields = ['email__contains', 'phone__contains', 'subject__contains']

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']
    search_fields = ['email__contains']

@admin.register(ApplyNow)
class ApplyNowAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'position', 'created_at', 'updated_at']
    search_fields = ['email__contains']

