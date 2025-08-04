from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    main_image = models.ImageField(upload_to='NewsAndArticles/', blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    author = models.CharField(max_length=120)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)

@receiver(post_delete, sender=Blog)
def post_save_blog_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.main_image.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Blog)
def pre_save_blog_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).main_image
        try:
            new_img = instance.main_image
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass

class GalleryCategorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    main_image = models.ImageField(upload_to='Gallery/', blank=True, null=True)
    category = models.ManyToManyField(GalleryCategorie)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + '--' + self.location

@receiver(post_delete, sender=Gallery)
def post_save_gallery_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.main_image.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Gallery)
def pre_save_gallery_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).main_image
        try:
            new_img = instance.main_image
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass

class ProjectCategorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='Projects/', blank=True, null=True)
    client = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    completion_date = models.DateField(blank=True, null=True)
    project_budget = models.CharField(max_length=255, blank=True, null=True)
    category = models.ManyToManyField(ProjectCategorie)
    content = models.TextField()
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + '--' + self.client

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Project, self).save(*args, **kwargs)

@receiver(post_delete, sender=Project)
def post_save_project_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.main_image.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Project)
def pre_save_project_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).main_image
        try:
            new_img = instance.main_image
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass

class PropertyAgent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + "--" + self.phone + "--" + self.email
    
class PropertyLocation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
PROPERY_TYPE_CHOICES = (
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    ('Interior', 'Interior'),
)

SALE_OR_RENT = (
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
)

class Propertie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=250, default=None)
    price = models.CharField(max_length=50, default=None)
    location = models.ForeignKey(PropertyLocation, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50, choices=PROPERY_TYPE_CHOICES, default=None)
    sale_or_rent = models.CharField(max_length=50, choices=SALE_OR_RENT, default=None)
    area = models.CharField(max_length=100, null=True, blank=True)
    main_image = models.ImageField(upload_to='Properties/', blank=True, null=True)
    agent = models.ManyToManyField(PropertyAgent, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + '--' + self.location.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Propertie, self).save(*args, **kwargs)

@receiver(post_delete, sender=Propertie)
def post_save_property_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.main_image.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Propertie)
def pre_save_property_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).main_image
        try:
            new_img = instance.main_image
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass
    
    
class PropertyEnquirie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    property = models.ForeignKey(Propertie,default=None, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + "--" + self.phone + "--" + self.email

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=255)
    preference = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + "--" + self.subject + "--" + self.preference

class NewsletterSubscriber(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.email

class ApplyNow(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=200)
    street_address = models.CharField(max_length=255)
    city_town = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    zip_code = models.BigIntegerField(null=True, blank=True)
    preference = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=150)
    resume = models.FileField(upload_to='Resume/')
    cover_letter = models.FileField(upload_to='CoverLetter/')
    education = models.TextField()
    work_experience = models.TextField()
    skills = models.TextField()
    references = models.TextField()
    additional_information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + '--' + self.first_name + '--' + self.last_name + '--' + str(self.phone) + '--' + self.email + '--' + self.position

@receiver(post_delete, sender=ApplyNow)
def post_save_apply_now_resume(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.resume.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=ApplyNow)
def pre_save_apply_now_resume(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).resume
        try:
            new_img = instance.resume
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass

@receiver(post_delete, sender=ApplyNow)
def post_save_apply_now_cover_letter(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.cover_letter.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=ApplyNow)
def pre_save_apply_now_cover_letter(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).cover_letter
        try:
            new_img = instance.cover_letter
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass
