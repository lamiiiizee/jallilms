import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ContactForm, EmailForm
from .models import Award,PositionsToken, Gallery, Update, YoutubeLink

# Create your views here.


def index(request):
    videos = YoutubeLink.objects.all()[:3]
    gallery = Gallery.objects.all()
    context = {"is_index": True, "videos": videos, "gallery": gallery}
    return render(request, "index.html", context)


def about(request):
    award = Award.objects.all()
    positionsToken = PositionsToken.objects.all()
    context = {"is_about": True, "award": award ,"positionsToken": positionsToken}
    return render(request, "about.html", context)


def position(request):
    context = {"is_position": True}

    return render(request, "positions.html", context)


def blog(request):
    youtube = YoutubeLink.objects.all()
    context = {"is_updates": True, "youtube": youtube}

    return render(request, "blog.html", context)


def updates(request, id):
    update = Update.objects.get(id=id)
    context = {"is_updates": True, "update": update}
    return render(request, "single-blog.html", context)


@csrf_exempt
def contact(request):
    template_name = "contact.html"
    forms = ContactForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            # return HttpResponse("successfully submitted")
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }

        else:
            response_data = {"status": "false", "title": "Form validation error", "message": repr(forms.errors)}
        return HttpResponse(json.dumps(response_data), content_type="application/javascript")
    else:
        context = {"form": forms, "is_contact": True}
    return render(request, template_name, context)


def email(request):
    template_name = "footer.html"
    emailform = EmailForm(request.POST or None)
    if request.method == "POST":
        if emailform.is_valid():
            data = emailform.save(commit=False)
            data.referral = "web"
            data.save()
            return HttpResponse("Successfully subscribed!!!")
        else:
            return HttpResponse("Failed to submit!! form validation error occurred!")
    else:
        context = {"emailform": emailform}
    return render(request, template_name, context)



def gallery(request):
    gallery = Gallery.objects.all()
    context = {"is_gallery": True, "gallery": gallery}
    return render(request, "gallery.html", context)