from django.db import models


# Create your models here.

class Heading(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Heading/", blank=False)
    service = models.ManyToManyField(to="Headingservice", blank=True, related_name="service")


class Headingservice(models.Model):
    title = models.CharField(max_length=30)


class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.FileField(upload_to="services/", blank=False)
    description = models.TextField()
    work_list = models.ManyToManyField(to="Work", blank=True, related_name="work_list")


class Work(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Works/", default="img.png")
    description = models.TextField(default="description here")
    url = models.URLField(blank=False)


class About(models.Model):
    image = models.ImageField(upload_to="About/", blank=False)
    details = models.TextField()
    name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11)
    career = models.CharField(max_length=30)


class CV(models.Model):
    cv = models.FileField(upload_to="CV", blank=False)
    timestamp = models.DateField(auto_now=True, auto_now_add=False)


class Skill(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=60)


class Education(models.Model):
    name = models.CharField(max_length=100)
    year_name = models.IntegerField(default=2014)
    group = models.CharField(max_length=30)
    org = models.CharField(max_length=200)
    hpa = models.FloatField(default=5.00)


class Mycareer(models.Model):
    clients = models.IntegerField(default=2)
    projects = models.IntegerField(default=2)
    award = models.IntegerField(default=2)
    experience = models.IntegerField(default=2)

class Contactinfo(models.Model):
    address=models.CharField(max_length=100)
    phone_1=models.CharField(max_length=11)
    phone_2=models.CharField(max_length=11)
    email_1=models.EmailField(max_length=40)
    email_2=models.EmailField(max_length=40)


class Socaillink(models.Model):
    fb=models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    instragam=models.URLField(blank=True)
    likedin=models.URLField(blank=True)
    skype=models.URLField(blank=True)

class Contactus(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField()
