from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("positions/", views.position, name="positions"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("email/", views.email, name="email"),
    path("updates/<int:id>", views.updates, name="updates"),
    path("gallery/", views.gallery, name="gallery"),

]
