from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('games', views.games, name='games'),
    path('games/tatteredtales', views.tatteredtales, name='tatteredtales'),
    path('home', views.home, name='home'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('search', views.search, name='search'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('termsandconditions', views.termsandconditions, name='termsandconditions')
]
