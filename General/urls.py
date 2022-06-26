from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('skills', views.skills, name='skills'),
    path('workEd', views.workEd, name='workEd'),
    path('tictactoe', views.tictactoe, name='tictactoe'),
    path('contact', views.contact, name='contact'),
    path('aStar', views.aStar, name='aStar'),
    path('resumebuilder', views.resumeBuilder, name='resumeBuilder'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('chatbotResponse', views.chatbotResponse, name='chatbotResponse'),
    path('passwordgenerator', views.PasswordGenerator, name='passwordGenerator'),
    path('weatherapp', views.WeatherApp, name='weatherApp'),
    path('weatherapprequest', views.WeatherAppRequest, name='weatherAppRequest')
]