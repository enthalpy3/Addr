from django.shortcuts import render

# Create your views here.

def name_list(request):
    return render(request, 'addr/name_list.html', {})