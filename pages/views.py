from django.shortcuts import render

from .models import Content


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def contact(request):
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


def news(request):
    context = {}
    return render(request, 'pages/news.html', context)


def privacypolicy(request):
    context = {}
    return render(request, 'pages/privacypolicy.html', context)


def search(request):
    content = Content()
    searchText = request.GET.get('searchText')
    displayText = content.search(searchText)

    context = {"searchText": searchText, "displayText": displayText}
    return render(request, 'pages/search.html', context)


def tatteredtales(request):
    context = {}
    return render(request, 'pages/games/tatteredtales.html', context)


def termsandconditions(request):
    context = {}
    return render(request, 'pages/termsandconditions.html', context)
