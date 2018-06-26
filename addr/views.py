from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Addr

def name_list(request):
    names = Addr.objects.all().order_by('name')
    return render(request, "addr/name_list.html", {'names': names})

def name_detail(request, pk):
    name = get_object_or_404(Addr, pk=pk)
    return render(request, 'addr/name_detail.html', {'name': name})