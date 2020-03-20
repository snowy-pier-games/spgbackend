from django.conf import settings
from django.shortcuts import render

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .forms import ContactForm, SubscribeForm
from .models import Content, InfoHandler


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def contact(request):
    displayText = ""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mail = Mail(
                from_email=email,
                to_emails='contact@snowypiergames.com',
                subject=subject,
                html_content=message)
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(mail)
                if response.status_code is 200 or response.status_code is 202:
                    displayText = "Your email was sent! We'll get back to you as soon as we can."
                else:
                    displayText = "Something went wrong... please send us an email at contact@snowypiergames.com"
            except Exception as e:
                displayText = "Something went wrong... please send us an email at contact@snowypiergames.com"
        else:
            displayText = form.errors

    context = {"displayText": displayText}
    return render(request, 'pages/contact.html', context)


def feed(request):
    context = {}
    return render(request, 'feed.html', context)


def games(request):
    context = {}
    return render(request, 'pages/games.html', context)


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


def privacypolicy(request):
    context = {}
    return render(request, 'pages/privacypolicy.html', context)


def search(request):
    content = Content()
    searchText = request.GET.get('searchText')
    displayText = content.search(searchText)

    context = {"searchText": searchText, "displayText": displayText}
    return render(request, 'pages/search.html', context)


def subscribe(request):
    displayText = ""

    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            infoHandler = InfoHandler()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            response = infoHandler.subscribeToMailchimp(email, name)

            if response.status_code is 200:
                displayText = "Thanks for subscribing!"
            elif "title" in response.json() and response.json()["title"] == "Member Exists":
                displayText = "Good news, you're already subscribed!"
            elif "detail" in response.json():
                displayText = response.json()["detail"]
            else:
                displayText = "Couldn't subscribe, status code " + str(response.status_code)
        else:
            displayText = form.errors

    context = {"displayText": displayText}
    return render(request, 'pages/subscribe.html', context)


def tatteredtales(request):
    context = {}
    return render(request, 'pages/games/tatteredtales.html', context)


def termsandconditions(request):
    context = {}
    return render(request, 'pages/termsandconditions.html', context)
