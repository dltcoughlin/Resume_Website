from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import projects.ChatbotProject.ChatbotResponse as chatbotReturn


def chatbotResponse(request):
    input = request.GET.get('text')
    data = chatbotReturn.chatbot_response(input)
    if request.is_ajax():
        return JsonResponse(data, safe=False)
# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def skills(request):
    return render(request, 'skills_page.html')

def tictactoe(request):
    return render(request, 'tic_tac_toe_page.html')
 
def aStar(request):
    return render(request, 'astar_page.html')

def chatbot(request):
    return render(request, 'chatbot_page.html')
    
def workEd(request):
    return render(request, 'wh_ed_page.html')
    
def contact(request):
    #pull contacts in database
    return render(request, 'contact_info_page.html')