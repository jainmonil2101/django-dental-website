from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'dental/home.html')


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
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')

        return render(request, 'dental/contact.html')


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
        return render(request, 'dental/home.html')
