from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect

from myapp.forms import ContactForm
from myapp.models import *
# Create your views here.
from protfolio import settings


def index(request):
    heading=Heading.objects.last()
    services=Service.objects.all()
    about=About.objects.last()
    my_cv=CV.objects.last()
    skil=Skill.objects.all()
    edu=Education.objects.all()
    my_car=Mycareer.objects.last()
    cont=Contactinfo.objects.last()
    socail=Socaillink.objects.last()
    if request.method=="POST":
        form=ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = EmailMessage(
                "Message received confirmation", "Someone try to contact you", to=[settings.EMAIL_HOST_USER, ]
            )
            email.send()
            messages.success(request, "Message Send successfully",extra_tags="contact")
            return redirect(request.POST['next'])
    else:
        form=ContactForm()
    context={
        'heading':heading,
        'services':services,
        'about':about,
        'my_cv':my_cv,
        'my_skill':skil,
        'my_education':edu,
        'my_car':my_car,
        'contact':cont,
        'socail':socail,
        'form':form,
    }
    return render(request,'index.html',context)