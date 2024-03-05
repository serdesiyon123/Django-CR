from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import viewForm
from .models import DB


def home(request):
    if request.method == 'GET':
        form = viewForm()
        return render(request, 'home.html', context={'form': form})
    else:
        form = viewForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
           form.save()
           return redirect('/list')




def list(request):
    li = DB.objects.all()

    return render(request,'list.html', {'li': li})


def all(request, store_id):
    store = DB.objects.get(pk=store_id)
    if store is not None:
        return render(request, 'store.html', {'store': store})
    else:
        raise Http404("Page does not exist")