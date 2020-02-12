from django.shortcuts import render

from .models import Content, InfoHandler


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    question = request.POST.get('question')
    # TODO: email question

    context = {}
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
    name = request.POST.get('name')
    email = request.POST.get('email')

    displayText = ""
    if email:
        infoHandler = InfoHandler()
        response = infoHandler.subscribeToMailchimp(email, name)

        if response.status_code is 200:
            displayText = "Thanks for subscribing!"
        elif "title" in response.json() and response.json()["title"] == "Member Exists":
            displayText = "Good news, you're already subscribed!"
        elif "detail" in response.json():
            displayText = response.json()["detail"]

    context = {"displayText": displayText}
    return render(request, 'pages/subscribe.html', context)


def tatteredtales(request):
    context = {}
    return render(request, 'pages/games/tatteredtales.html', context)


def termsandconditions(request):
    context = {}
    return render(request, 'pages/termsandconditions.html', context)
