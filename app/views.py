from datetime import datetime
from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests
from app import models

def home(request):
    API_KEY = open("API_KEY.txt", "r").read()

    context = {
        'title':'Home Page',
        'year':datetime.now().year,
      }
    
    if request.method == "POST":
      city = request.POST['city']
      current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
      
      weather_data = fetch_weather_and_forecast(city, API_KEY, current_weather_url)
      
      context['weather_data'] = weather_data
      
      return render_home(request, context)
    else:
      return render_home(request, context)

def render_home(request, context):
  """Renders the home page."""
  assert isinstance(request, HttpRequest)
  return render(
          request,
          'app/home/index.html',
          context
      ) 

def redirect_home():
  """ReDirect the home page."""
  return redirect("home")

def fetch_weather_and_forecast(city, api_key, current_weather_url):
  response = requests.get(current_weather_url.format(city, api_key)).json()
  
  weather_data = {
      "city":city,
      "temperature": round(response['main']['temp'] - 273.15, 2),
      "description": response['weather'][0]['description'],
      "icon": response['weather'][0]['icon']
    }
    
  return weather_data

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def login(request):
  context = {
          'year':datetime.now().year,
        }
  
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    
    user_exist = models.User().exist_user(username)

    if(user_exist):
      context['title'] = "Home Page"
      context['this_user'] = username
      return redirect_home()
    else:
      context['title'] = "Login"
      return redirect_login()
    
      
  else:
    context['title'] = "Login"
   
    return render_login(request, context)

def render_login(request, context):
  """Renders the login page."""
  assert isinstance(request, HttpRequest)
  return render(
          request,
          'app/account/login/login.html',
          context,
          
      )

def redirect_login():
  """ReDirect the login page."""
  return redirect("login")

def signup(request):
  context = {
          'year':datetime.now().year,
        }
  
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    gmail = request.POST['gmail']
    
    iswritten = models.User().write_user(username, password, gmail)
    
    if iswritten:  
      context['title'] = "Login"
      return redirect_login()
    else:
      context['title'] = "Sign Up"
      context["signed_up"] = "false"
      return render_signup(request, context)
    
  else:
    context['title'] = "Sign Up"
    return render_signup(request, context)

def render_signup(request, context):
  """Renders the sign-up page."""
  assert isinstance(request, HttpRequest)
  return render(
          request,
          'app/account/signup/index.html',
          context
      )

def redirect_signup():
  """ReDirect the signup page."""
  return redirect("signup")

