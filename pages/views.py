from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def news(request):
    context = {}
    return render(request, 'pages/news.html', context)


def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)


def games(request):
    context = {}
    return render(request, 'pages/games.html', context)


def tatteredtales(request):
    context = {}
    return render(request, 'pages/games/tatteredtales.html', context)
