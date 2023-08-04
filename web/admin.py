from django.contrib import admin

from .models import Award,PositionsToken, Contact, Email, Gallery, Notification, Update, YoutubeLink


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    pass

@admin.register(PositionsToken)
class PositionsTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(YoutubeLink)
class YoutubeLinAdmin(admin.ModelAdmin):
    list_display = ("title", "video_id", "video_url", "timestamp")
