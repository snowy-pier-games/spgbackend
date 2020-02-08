from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('games', views.games, name='games'),
    path('games/tatteredtales', views.tatteredtales, name='tatteredtales'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('termsandconditions', views.termsandconditions, name='termsandconditions'),
    path('search', views.search, name='search')
]
