from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else :
        form = RegisterForm()
    template = loader.get_template('register.html')
    context = { 'form': form }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user :
                login(request, user)
                return redirect('event_calendar')
    else:
        form = LoginForm()
    template = loader.get_template('login.html')
    context = { 'form': form }
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    template = loader.get_template('account_master.html')
    context = {}
    return HttpResponse(template.render(context, request))