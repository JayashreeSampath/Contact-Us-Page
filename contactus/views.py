from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import contact
from .forms import details

# Create your views here.


def index(request):
    template = loader.get_template('contactus/index.html')
    return HttpResponse(template.render({}, request))


def add(request):
    a = request.POST['name']  # [] has input tag's name
    b = request.POST['mail']
    c = request.POST['sub']
    d = request.POST['msg']
    sample = contact(Name=a, Mail=b, Sub=c, Msg=d)
    sample.save()
    # return render(request, 'contactus/index.html', {})
    return HttpResponseRedirect(reverse(index))
