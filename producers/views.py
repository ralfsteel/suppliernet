from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from producers.models import Client, Pricelist, Promotional
from producers.forms import RegisterForm, LoginForm


def customer(request):
    context = RequestContext(request)
    client_lists = Client.objects.all().order_by('number')

    context_dict = {
        'client_lists': client_lists,
    }

    return render_to_response('producers/customer.html', context_dict, context)

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            registered = True
        else:
            print form.errors
    else:
        form = RegisterForm()

    context_dict = {
        'form': form,
        'registered': registered
    }

    return render_to_response('producers/register.html', context_dict, context)

def login(request):
    context = RequestContext(request)
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("logged in")
            else:
                return HttpResponse("Credentials not correct")


    context_dict = {
        'form': form,
    }

    return render_to_response('producers/login.html', context_dict, context)

def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/producers/')



