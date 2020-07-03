from django.shortcuts import render
from django.http import HttpResponse
from .models import Paint, Category, User
from django.core.mail import send_mail



def singleSlug(request,singleSlug):
    categories = [c.category_slug for c in Category.objects.all()]
    if singleSlug in categories:
       HttpResponse("cat")


def home(request):
    return render(request=request,
                  template_name="gallery/home.html",
                  context={
                      "categories": Category.objects.all,
                      "sample": Paint.objects.all
                  })


def gallery(request):
    return render(request=request,
                  template_name="gallery/gallery.html",
                  context={"paints": Paint.objects.all})


def about(request):
    return render(
        request=request,
        template_name="gallery/about.html",
        context={"details": User.objects.all}
    )


def cat(request):
    return render(
        request=request,
        template_name="gallery/category.html",
        context={
            "cat":Category.objects.all
        }
    )


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return render(request,template_name='gallery/about.html',context={'name':name})

        send_mail(name,message,email,[bawanthanianuththara@gmail.com,nkindelpitiya@gmail.com],fail_silently=False)
    else:
        return HttpResponse("Not Successs")
