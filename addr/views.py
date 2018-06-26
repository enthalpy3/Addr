from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from addr.form import AddrForm
from .models import Addr


def name_list(request):
    names = Addr.objects.all().order_by('name')
    return render(request, "addr/name_list.html", {'names': names})

@login_required
def name_detail(request, pk):
    name = get_object_or_404(Addr, pk=pk)
    return render(request, 'addr/name_detail.html', {'name': name})

@login_required
def name_new(request):
    if request.method == "POST":
        form = AddrForm(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            # name.author = request.user
            name.created_date = timezone.now()
            name.save()
            return redirect('addr:name_detail', pk=name.pk)
    else:
        form = AddrForm()
    return render(request, 'addr/name_edit.html', {'form': form})

@login_required
def name_edit(request, pk):
    name = get_object_or_404(Addr, pk=pk)
    if request.method == "POST":
        form = AddrForm(request.POST, instance=name)
        if form.is_valid():
            name = form.save(commit=False)
            # post.author = request.user
            name.created_date = timezone.now()
            name.save()
            return redirect('addr:name_detail', pk=name.pk)
    else:
        form = AddrForm(instance=name)
    return render(request, 'addr/name_edit.html', {'form': form})

@login_required
def name_draft_list(request):
    names = Addr.objects.all().order_by('name')
    return render(request, 'addr/name_draft_list.html', {'names': names})

@login_required
def name_publish(request, pk):
    name = get_object_or_404(Addr, pk=pk)
    name.publish()
    return redirect('addr:name_detail', pk=pk)

@login_required
def name_remove(request, pk):
    name = get_object_or_404(Addr, pk=pk)
    name.delete()
    return redirect('addr:name_list')

@login_required
def name_approve(request, pk):
    name = get_object_or_404(Addr, pk=pk)
    name.approve()
    return redirect('addr:name_detail', pk=name.pk)

