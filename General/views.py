from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def skills(request):
    return render(request, 'skills_page.html')

def tictactoe(request):
    return render(request, 'tic_tac_toe_page.html')
 
def aStar(request):
    return render(request, 'astar_page.html')
    
def workEd(request):
    return render(request, 'wh_ed_page.html')
    
def contact(request):
    #pull contacts in database
    return render(request, 'contact_info_page.html')