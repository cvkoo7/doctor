from django.shortcuts import render

from dentist.models import feedback


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def blog_details(request):
    return render(request, "blog-details.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        ins = feedback(name=name, email=email, subject=subject)
        ins.save()
    return render(request, "contact.html")


def index(request):
    return render(request, "index.html")


def pricing(request):
    return render(request, "pricing.html")


def service(request):
    return render(request, "service.html")


def retrieveInf(request):
    if request.user.is_authenticated:
        data1 = feedback.objects.all()
        context = {'data': data1}
        return render(request, "retrieveInf.html", context)
    else:
        return render(request, "index.html")

