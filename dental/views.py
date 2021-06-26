from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'dental/home.html', {'email': settings.EMAIL_HOST_USER, 'password': settings.EMAIL_HOST_PASSWORD})


def about(request):
    return render(request, 'dental/about.html')


def service(request):
    return render(request, 'dental/service.html')


def pricing(request):
    return render(request, 'dental/pricing.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'dental/contact.html')
    else:
        name = request.POST.get('message-name')
        email = request.POST.get('message-email')
        message = request.POST.get('message')

        send_mail(name, message, email, [settings.EMAIL_HOST_USER], fail_silently=False)

        return render(request, 'dental/contact.html', {'name': name})


def appointment(request):
    if request.method == 'GET':
        return render(request, 'dental/home.html')
    else:
        name = request.POST.get('your-name')
        phone = request.POST.get('your-phone')
        email = request.POST.get('your-email')
        date_time = request.POST.get('your-date-time')
        message = request.POST.get('your-message')

        new_message = f'''
        Name: {name}
        Phone: {phone}
        Schedule: {date_time}
        Message: {message}
        '''

        send_mail('Appointment Request', new_message,
                  email, [settings.EMAIL_HOST_USER],fail_silently=False)
        return render(request, 'dental/appointment.html', {
            'name': name,
            'phone': phone,
            'email': email,
            'date_time': date_time,
            'message': message,
        })
