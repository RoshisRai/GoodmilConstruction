from django.urls import path
from .views import home, about, blog, blog_post, blog_search, contact_us, gallery, projects, project_page, realestate, realestate_page, realestate_search, services, newsletter_subscriber, add_to_projects, apply, realestate_enquiry, add_to_properties, filtered_realestate

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog-post/<slug:slug>', blog_post, name='blog-post'),
    path('blog-search/', blog_search, name='blog-search'),
    path('contact-us/', contact_us, name='contact-us'),
    path('gallery/', gallery, name='gallery'),
    path('projects/', projects, name='projects'),
    path('project-page/<slug:slug>', project_page, name='project-page'),
    path('add-to-projects/', add_to_projects, name="add-to-projects"),
    path('realestate/', realestate, name='realestate'),
    path('realestate-page/<slug:slug>', realestate_page, name='realestate-page'),
    path('realestate-search/', realestate_search, name='realestate-search'),
    path('realestate-enquiry/', realestate_enquiry, name='realestate-enquiry'),
    path('add-to-properties', add_to_properties, name='add-to-properties'),
    path('filtered-realestate', filtered_realestate, name='filtered-realestate'),
    path('services/', services, name='services'),
    path('newsletter-subscriber/', newsletter_subscriber, name='newsletter-subscriber'),
    path('apply/', apply, name='apply'),
]