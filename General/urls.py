from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('skills', views.skills, name='skills'),
    path('workEd', views.workEd, name='workEd'),
    path('tictactoe', views.tictactoe, name='tictactoe'),
    path('contact', views.contact, name='contact'),
    path('aStar', views.aStar, name='aStar'),
]