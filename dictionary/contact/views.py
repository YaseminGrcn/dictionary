from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from dictionary.users.models import User
# Create your views here.


def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        mail = User.objects.get(username=request.user).email
        if from_email and message and from_email:
            try:
                send_mail(subject, message, from_email, [mail], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Mail gonderme islemi basarili...')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, "messages/messages.html")

def thanks(request):
    return render(request, "messages/thanks.html")
