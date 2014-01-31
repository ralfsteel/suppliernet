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
    registerd = False
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
        'registered': registerd
    }

    return render_to_response('producers/register.html', context_dict, context)

def login(request):
    context = RequestContext(request)
    form = LoginForm(data=request.POST)

    if request.method == 'POST':

        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(name=name, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("logged in")
        else:
            print form.errors
    else:
        form = LoginForm()
    context_dict = {
        'form': form,

    }

    return render_to_response('producers/login.html', context_dict, context)


