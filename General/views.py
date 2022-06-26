from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from General.scripts.buildResume import buildPDF
import json, requests
import General.scripts.chatbotProject.ChatbotResponse as chatbotReturn

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def chatbotResponse(request):
    input = request.GET.get('text')
    data = chatbotReturn.chatbot_response(input)
    if is_ajax(request=request):
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

def resumeBuilder(request):
    #pull contacts in database
    if request.method == "POST":
        buildPDF(json.dumps(request.POST))
    return render(request, 'resumeBuilder.html')

def PasswordGenerator(request):
    return render(request, 'password_generator.html')

def WeatherApp(request):
    return render(request, 'weather_app.html')

def WeatherAppRequest(request):
    apiKey = "667f94fa87425eaae30033d2e408caf0"
    zipCode = request.GET.get('text')
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    fullUrl = baseUrl + "appid=" + apiKey + "&zip=" + zipCode + '&units=imperial'
    response = requests.get(fullUrl)
    responseData = response.json()
    return JsonResponse(responseData, safe=False)