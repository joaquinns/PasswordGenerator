from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
import random 

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def password(request):
  characters = list('qwertyuiopasdfghjklñzxcvbnm')
  generated_password = ''
  length = int(request.GET.get('length'))

  if request.GET.get('uppercase'):
    characters.extend(list('QWERTYUIOPASDFGHJKLÑZXCVBNM'))
  
  if(request.GET.get('characters')):
    characters.extend(list('!#$%&()=?¡<>-_[]*'))

  if(request.GET.get('numbers')):
    characters.extend(list('1234567890'))
  

  for char in range(length):
    generated_password += random.choice(characters)


  return render(request, 'password.html', {'password': generated_password})