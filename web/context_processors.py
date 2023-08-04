from .forms import EmailForm
from .models import Notification, Update


def extras(request):
    update = Update.objects.all()
    notification = Notification.objects.all()
    emailform = EmailForm()

    return {"updates": update, "emailform": emailform, "notification": notification}
