from django.conf import settings
from django.shortcuts import render

import json
import requests

from .models import Content


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def contact(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    question = request.GET.get('question')
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
    name = request.GET.get('name')
    email = request.GET.get('email')

    api_url = f'https://{settings.MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
    members_endpoint = f'{api_url}/lists/{settings.MAILCHIMP_AUDIENCE_ID}/members'

    data = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {
            "FNAME": name
        }
    }

    r = requests.post(
        members_endpoint,
        auth=("", settings.MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )

    context = {}
    return render(request, 'pages/subscribe.html', context)


def tatteredtales(request):
    context = {}
    return render(request, 'pages/games/tatteredtales.html', context)


def termsandconditions(request):
    context = {}
    return render(request, 'pages/termsandconditions.html', context)
