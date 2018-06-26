from django.shortcuts import render
from django.utils import timezone
from .models import Addr

def name_list(request):
    names = Addr.objects.all().order_by('name')
    return render(request, "addr/name_list.html", {'names': names})