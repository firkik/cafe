from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import *


def catalog_list(request):
    model = Product.objects.filter(exists = True)
    context = {
        'dish_list': model
    }
    return render(request, 'cafe/main/index.html', context)


def dish(request, id):
    model = get_object_or_404(Product, pk=id)
    context = {
        'dish': model
    }
    return render(request, 'cafe/dish/dish.html', context)


def all_provider(request):
    model = Provider.objects.all()
    context = {
        'all_provider': model
    }
    return render(request, 'cafe/provider/main/all.html', context)


def provider(request, id):
    model = get_object_or_404(Provider, pk=id)
    context = {
        'provider': model
    }
    return render(request, 'cafe/provider/provider/provider.html', context)


def add_provider(request):
    if request.method == 'POST':
        form_add_provider = ProviderForm(request.POST)
        if form_add_provider.is_valid() and form_add_provider.clean_telephone():
            new_provider = Provider(**form_add_provider.cleaned_data)
            new_provider.save()
            return redirect('all_provider_list')
        return render(request, 'cafe/provider/provider/add_provider.html', {'form': ProviderForm, 'error': 'error code'})
    else:
        form = ProviderForm
        context = {
            'form': form
        }
        return render(request, 'cafe/provider/provider/add_provider.html', context)