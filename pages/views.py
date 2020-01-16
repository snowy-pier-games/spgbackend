from django.shortcuts import render

from .models import Content




def home(request):
    context = {"displayText": Content.displayText["home"]}
    return render(request, 'pages/home.html', context)


def about(request):
    context = {"displayText": Content.displayText["about"]}
    return render(request, 'pages/about.html', context)


def news(request):
    context = {"displayText": Content.displayText["news"]}
    return render(request, 'pages/news.html', context)


def contact(request):
    context = {"displayText": Content.displayText["contact"]}
    return render(request, 'pages/contact.html', context)


def games(request):
    context = {"displayText": Content.displayText["games"]}
    return render(request, 'pages/games.html', context)


def tatteredtales(request):
    context = {"displayText": Content.displayText["games/tatteredtales"]}
    return render(request, 'pages/games/tatteredtales.html', context)

def feed(request):
    context = {"displayText": Content.displayText["feed"]}
    return render(request, 'feed.html', context)

def search(request):
    searchText = request.GET.get('searchText')
    displayText = ""

    for page, pageText in Content.displayText.items():
        textBegin = pageText.find(searchText)
        if textBegin > -1:
            textEnd = textBegin + len(searchText)
            lookBehind = max(0, textBegin - 64)
            lookAhead = min(len(pageText), textEnd + 64)

            prefix = ""
            suffix = ""
            if lookBehind > 0:
                prefix = "..."
            if lookAhead < len(pageText):
                suffix = "..."

            displayText += "<h3><a href='/" + page + "'>" + page + "</a></h3>"
            displayText += "<p>" + prefix + pageText[lookBehind:textBegin] \
                           + "<span style='color:red;'>" + searchText + "</span>" \
                           + pageText[textEnd:lookAhead] + suffix + "</p>"

    if not displayText:
        displayText = "No results"

    context = {"searchText": searchText, "displayText": displayText}
    return render(request, 'pages/search.html', context)
