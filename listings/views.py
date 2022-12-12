from django.shortcuts import render
from django.shortcuts import redirect
from .models import Listings
from .forms import ListingsForm

# CRUD - create, retrieve, update, delete - list

def listing_list(request):
    listings = Listings.objects.all()
    context = {
        'listings' : listings
    }
    return render(request, 'listings.html', context)

def listing_retrieve(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listing.html', context)

def listing_create(request):
    form = ListingsForm()
    if request.method == 'POST':
        form = ListingsForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listings/')
    context = {
        'form': form
    }
    return render(request, 'listing_create.html', context)

def listing_update(request, pk):
    listing = Listings.objects.get(id=pk)
    form = ListingsForm(instance=listing)
    if request.method == 'POST':
        form = ListingsForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings/')
    context = {
        'form': form
    }
    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect('/listings/')
