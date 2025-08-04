from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Gallery, Blog, NewsletterSubscriber, Project, ContactUs, ApplyNow, Propertie, PropertyEnquirie, PropertyLocation
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q


def validate_email_address(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    
# Create your views here.
def home(request):
    gallery = Gallery.objects.all().order_by('-id')[:6]
    blogs = Blog.objects.all().order_by('-id')[:3]
    projects = Project.objects.all().order_by('-id')[:8]
    properties = Propertie.objects.all().order_by('?')[:6]
    context = {
        'gallery': gallery,
        'blogs': blogs,
        'projects': projects,
        'properties': properties,
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    left_blog = Blog.objects.all().order_by('-id')[:1][0]
    right_blogs = Blog.objects.all().order_by('-id')[1:3]
    blogs = Blog.objects.all().order_by('-id')
    top_three_slugs = [left_blog.slug]
    for i in right_blogs:
        top_three_slugs.append(i.slug)
    main_blogs = []
    for i in blogs:
        if i.slug not in top_three_slugs:
            main_blogs.append(i)
    random_blogs = Blog.objects.all().order_by('?')
    other_blogs = []
    for i in random_blogs:
        if i.slug not in top_three_slugs:
            other_blogs.append(i)
    context = {
        'left_blog': left_blog,
        'right_blogs': right_blogs,
        'main_blogs': main_blogs,
        'other_blogs': other_blogs[:4]
    }
    return render(request, 'home/blog.html', context)

def blog_post(request, slug):
    blog = Blog.objects.get(slug=slug)
    prev_blog_slug = next_blog_slug = None
    if Blog.objects.filter(id=blog.id-1).exists():
        prev_blog_slug = Blog.objects.get(id=blog.id-1).slug
    if Blog.objects.filter(id=blog.id+1).exists():
        next_blog_slug = Blog.objects.get(id=blog.id+1).slug

    blog_category_list = blog.categories.split(" ")
    related_blogs = []
    for i in blog_category_list:
        blog_filter = Blog.objects.filter(categories__icontains=i).order_by('-id')
        for j in blog_filter:
            if j not in related_blogs:
                if j.slug != blog.slug:
                    related_blogs.append(j)
    other_blogs = Blog.objects.all().order_by('-id')[:4]
    context = {
        'blog' : blog,
        'related_blogs': related_blogs[:3],
        'other_blogs': other_blogs,
        'prev_blog_slug': prev_blog_slug,
        'next_blog_slug': next_blog_slug,
    }
    return render(request, 'home/blogpost.html', context)

def blog_search(request):
    query = request.GET.get('blog-search')
    context = {
        'query': query,
    }
    if(len(query) <= 3):
        messages.error(request, 'Cound not find any matches. The number of search words is too small.')
    elif(len(query)>= 120):
        messages.error(request, 'The query length is above 120. Please! make it shorter.')
    else:
        blog1 = Blog.objects.filter(title__icontains=query)
        blog2 = Blog.objects.filter(sub_title__icontains=query)
        blog3 = Blog.objects.filter(categories__icontains=query)
        blog4 = Blog.objects.filter(author__icontains=query)
        blog5 = Blog.objects.filter(content__icontains=query)
        blogst = blog1.union(blog2)
        blognd = blogst.union(blog3)
        blogrd = blognd.union(blog4)
        blogs = blogrd.union(blog5)
        context['blogs'] = blogs
    return render(request, 'home/blogsearch.html', context)

def gallery(request):
    gallery = Gallery.objects.all().order_by('-id')
    context = {
        'gallery': gallery
    }
    return render(request, 'home/gallery.html', context)

def projects(request):
    projects = Project.objects.all().order_by('-id')[:6]
    context = {
        'projects': projects,
    }
    return render(request, 'home/projects.html', context)

@csrf_exempt
def add_to_projects(request):
    if request.method == 'POST':
        last_id = int(request.POST.get('lastId'))
        filter_projects = Project.objects.filter(id__lt=last_id).order_by('-id')[:6]
        projects = {}
        for i in filter_projects:
            projects[i.id] = {
                'project_id': i.id,
                'project_title': i.title,
                'project_location': i.location,
                'project_image_url': i.main_image.url,
                'project_category': ' '.join([c.name for c in i.category.all()]),
                'project_url': f"/project-page/{i.slug}"
            }
        if len(projects) == 0:
            return JsonResponse({'error_message': 'There are no other available projects to showcase.'})
        else:
            context = {
                'projects' : projects
            }
            return JsonResponse(context)

def project_page(request, slug):
    project = Project.objects.get(slug=slug)
    prev_project_slug = next_project_slug = None
    if Project.objects.filter(id=project.id-1).exists():
        prev_project_slug = Project.objects.get(id=project.id-1).slug
    if Project.objects.filter(id=project.id+1).exists():
        next_project_slug = Project.objects.get(id=project.id+1).slug
    projects = Project.objects.all().order_by('-id')
    recent_projects = []
    for i in projects:
        if i.slug != project.slug:
            recent_projects.append(i)
    context = {
        'project': project,
        'prev_project_slug': prev_project_slug,
        'next_project_slug': next_project_slug,
        'recent_projects': recent_projects[:3],
    }
    return render(request, 'home/projectpage.html', context)

def realestate(request):
    properties = Propertie.objects.all().order_by('-id')[:6]
    property_locations = PropertyLocation.objects.all()
    context = {
        'properties': properties,
        'property_locations': property_locations,
    }
    return render(request, 'home/realestate.html', context)

@csrf_exempt
def filtered_realestate(request):
    if request.method == 'POST':
        property_location = request.POST.get('propertyLocation')
        property_type = request.POST.get('propertyType')
        property_sale_or_rent = request.POST.get('propertySaleOrRent')
        print(property_location, property_type, property_sale_or_rent)
        if property_location == "" and property_type == "" and property_sale_or_rent == "":
            context = {'error_message': 'You have not selected any filters.'}
        else:
            properties = {}
            if property_location != "" and property_type == "" and property_sale_or_rent == "":
                p_location = PropertyLocation.objects.filter(name__iexact=property_location)
                print(p_location)
                filter_properties = Propertie.objects.filter(location__in=p_location)
            elif property_location != "" and property_type != "" and property_sale_or_rent == "":
                p_location = PropertyLocation.objects.filter(name__iexact=property_location)
                filter_properties = Propertie.objects.filter(Q(location__in=p_location) & Q(property_type__exact=property_type))
            elif property_location != "" and property_type == "" and property_sale_or_rent != "":
                p_location = PropertyLocation.objects.filter(name__iexact=property_location)
                filter_properties = Propertie.objects.filter(Q(location__in=p_location) & Q(sale_or_rent__exact=property_sale_or_rent))
            elif property_location == "" and property_type != "" and property_sale_or_rent == "":
                filter_properties = Propertie.objects.filter(property_type__exact=property_type)
            elif property_location == "" and property_type != "" and property_sale_or_rent != "":
                filter_properties = Propertie.objects.filter(Q(property_type__exact=property_type) & Q(sale_or_rent__exact=property_sale_or_rent))
            elif property_location == "" and property_type == "" and property_sale_or_rent != "":
                filter_properties = Propertie.objects.filter(sale_or_rent__exact=property_sale_or_rent)
            elif property_location != "" and property_type != "" and property_sale_or_rent != "":
                p_location = PropertyLocation.objects.filter(name__iexact=property_location)
                p_location_all = PropertyLocation.objects.filter(name__iexact="All Over Nepal")
                if property_location != 6 and property_type == "Interior":
                    filter_properties = Propertie.objects.filter((Q(location__in=p_location) | Q(location__in=p_location_all)) & Q(property_type__exact=property_type))
                else:
                    filter_properties = Propertie.objects.filter(Q(location__in=p_location) & Q(property_type__exact=property_type) & Q(sale_or_rent__exact=property_sale_or_rent))
            for i in filter_properties:
                properties[i.id] = {
                    'property_id': i.id,
                    'property_title': i.title,
                    'property_sub_title': i.sub_title,
                    'property_image_url': i.main_image.url,
                    'property_price': i.price,
                    'property_area': i.area,
                    'property_sale_or_rent': i.sale_or_rent,
                    'property_url': f"/realestate-page/{i.slug}"
                }
            print(properties)
            context = {'properties': properties}
        return JsonResponse(context)

def realestate_page(request, slug):
    property = Propertie.objects.get(slug=slug)
    prev_property_slug = next_property_slug = None
    if Project.objects.filter(id=property.id-1).exists():
        prev_property_slug = Propertie.objects.get(id=property.id-1).slug
    if Project.objects.filter(id=property.id+1).exists():
        next_property_slug = Propertie.objects.get(id=property.id+1).slug
    context = {
        'property': property,
        'prev_property_slug': prev_property_slug,
        'next_property_slug': next_property_slug,
    }
    return render(request, 'home/realestatepage.html', context)

def realestate_enquiry(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if validate_email_address(email):
            phone = request.POST.get('phone')
            if len(phone) == 10:
                name = request.POST.get('name')
                property_id = request.POST.get('property')
                property = Propertie.objects.get(id=property_id)
                property_enquiry = PropertyEnquirie.objects.create(name=name, email=email, phone=phone, property=property)
                property_enquiry.save()
                messages.success(request, 'Success!! We will get back to you soon!!')
            else:
                messages.error(request, 'Please enter a valid phone number. Thank you!')
        else:
            messages.error(request, 'Please enter a valid email address. Thank you!')
    return HttpResponseRedirect(request. META['HTTP_REFERER'])

def realestate_search(request):
    query = request.GET.get('property-search')
    context = {
        'query': query,
    }
    if(len(query) <= 3):
        messages.error(request, 'Cound not find any matches. The number of search words is too small.')
    elif(len(query)>= 120):
        messages.error(request, 'The query length is above 120. Please! make it shorter.')
    else:
        property1 = Propertie.objects.filter(title__icontains=query)
        property2 = Propertie.objects.filter(sub_title__icontains=query)
        property3 = Propertie.objects.filter(property_type__icontains=query)
        property4 = Propertie.objects.filter(content__icontains=query)
        propertyst = property1.union(property2)
        propertynd = propertyst.union(property3)
        properties = propertynd.union(property4)
        context['properties'] = properties
    return render(request, 'home/realestatesearch.html', context)

@csrf_exempt
def add_to_properties(request):
    if request.method == 'POST':
        last_id = int(request.POST.get('lastId'))
        filter_properties = Propertie.objects.filter(id__lt=last_id).order_by('-id')[:6]
        properties = {}
        print('hello')
        for i in filter_properties:
            properties[i.id] = {
                'property_id': i.id,
                'property_title': i.title,
                'property_sub_title': i.sub_title,
                'property_image_url': i.main_image.url,
                'property_price': i.price,
                'property_area': i.area,
                'property_sale_or_rent': i.sale_or_rent,
                'property_url': f"/realestate-page/{i.slug}"
            }
        if len(properties) == 0:
            print('no properties')
            return JsonResponse({'error_message': 'There are no other available properties to showcase.'})
        else:
            context = {
                'properties' : properties
            }
            return JsonResponse(context)

def services(request):
    return render(request, 'home/services.html')

def contact_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if validate_email_address(email):
            phone = request.POST.get('phone')
            if len(phone) == 10:
                name = request.POST.get('name')
                preference = request.POST.get('preference', '')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                contact = ContactUs(name=name, email=email, phone=phone, subject=subject, preference=preference, message=message)
                contact.save()
                messages.success(request, 'Your message has been sent successfully!!')
            else:
                messages.error(request, 'Please enter a valid phone number. Thank you!')
            return HttpResponseRedirect(request. META['HTTP_REFERER'])
        else:
            messages.error(request, 'Please enter a valid email address. Thank you!')
        return HttpResponseRedirect(request. META['HTTP_REFERER'])
    elif request.method == 'GET':
        return render(request, 'home/contactus.html')

def newsletter_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('subscribe-email')
        if validate_email_address(email):
            NewsletterSubscriber(email=email).save()
            messages.success(request, 'Thank you for subscribing Goodmil Construction')
        else:
            messages.error(request, 'Please enter a valid email address. Thank you!')
        return HttpResponseRedirect(request. META['HTTP_REFERER'])

def apply(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if validate_email_address(email):
            phone = request.POST.get('phone')
            if len(phone) == 10:
                first_name = request.POST.get('first-name')
                last_name = request.POST.get('last-name')
                street_address = request.POST.get('street-address')
                city_town = request.POST.get('city-town')
                district = request.POST.get('district')
                zip_code = request.POST.get('zip-code', '')
                preference = request.POST.get('preference', '')
                position = request.POST.get('position')
                resume = request.FILES.get('resume')
                cover_letter = request.FILES.get('cover-letter')
                education = request.POST.get('education')
                work_experience = request.POST.get('work-experience')
                skills = request.POST.get('skills')
                references = request.POST.get('references')
                additional_info = request.POST.get('additional-info')
                apply_now = ApplyNow(first_name=first_name, last_name=last_name, email=email, phone=phone, street_address=street_address, city_town=city_town, district=district, zip_code=zip_code, preference=preference, position=position, resume=resume, cover_letter=cover_letter, education=education, work_experience=work_experience, skills=skills, references=references, additional_information=additional_info)
                apply_now.save()
                print(first_name, last_name, email, phone, street_address, city_town, district, zip_code, preference, position, resume, cover_letter, education, work_experience, skills, references, additional_info)
                messages.success(request, 'Your have successfully applied for a job with goodmil construction. We will get back to you soon!!')
            else:
                messages.error(request, 'Please enter a valid phone number. Thank you!')
        return redirect('home')
    else:
        return render(request, 'home/apply.html')