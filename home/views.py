from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Property, PropertyImage, PropertyType, PropertyNeighborhood, PropertyPricerange, Search, Profile, \
    Event
from .forms import RegistrationForm, PropertyForm, EventForm, ProfileForm
from django.urls import reverse
import os
from django.utils import timezone
from django.db.models import Count
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid login credentials"
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def home_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    # featured_Property = Property.objects.get(featured_property=True)
    #  images = PropertyImage.objects.filter(property_id=featured_Property.id)
    # return render(request, 'home.html', {'property': featured_Property,
    # 'images': images})
    properties = Property.objects.get(featured_property=True)

    context = {
        'properties': properties,
    }
    return render(request, 'home.html', context)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:event')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


def event_view(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'event.html', context)


def profile_view(request):
    profile = get_object_or_404(Profile)
    context = {'profile': profile}
    return render(request, 'profile.html', context)


def listing_view(request):
    listings = Property.objects.filter(flag=True)
    context = {'listings': listings}
    return render(request, 'listings.html', context)


def detail_view(request, pk):
    details = get_object_or_404(Property, pk=pk)
    context = {'details': details}
    return render(request, 'details.html', context)


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['featured_property']:
                # Set existing featured property to False
                Property.objects.filter(featured_property=True).update(featured_property=False)
            form.save()
            return redirect('home:listings')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


def edit_property(request, pk):
    property = Property.objects.get(id=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            if form.cleaned_data['featured_property']:
                # Set existing featured property to False
                Property.objects.filter(featured_property=True).update(featured_property=False)
            form.save()
            return redirect('home:listings')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'edit_property.html', {'form': form})


def property_search(request):
    property_types = PropertyType.objects.all()
    neighborhoods = PropertyNeighborhood.objects.all()
    price_ranges = PropertyPricerange.objects.all()
    properties = Property.objects.filter(flag=True)

    searched_property = request.GET.get('property_type')
    searched_neighbourhood = request.GET.get('property_neighborhood')
    searched_pricerange = request.GET.get('property_price_range')

    if request.GET.get('property_type'):
        properties = properties.filter(property_type=request.GET.get('property_type'))
        Search.objects.create(date=timezone.now(), property_type_id=request.GET.get('property_type'))
    elif request.GET.get('property_neighborhood'):
        properties = properties.filter(property_neighborhood=request.GET.get('property_neighborhood'))
        Search.objects.create(date=timezone.now(), property_neighborhood_id=request.GET.get('property_neighborhood'))
    elif request.GET.get('property_price_range'):
        properties = properties.filter(property_type_price_range=request.GET.get('property_price_range'))
        Search.objects.create(date=timezone.now(), property_type_price_range_id=request.GET.get('property_price_range'))
    context = {
        'property_types': property_types,
        'neighborhoods': neighborhoods,
        'price_ranges': price_ranges,
        'properties': properties,
        'searched_property': searched_property,
        'searched_neighbourhood': searched_neighbourhood,
        'searched_pricerange': searched_pricerange,
    }

    return render(request, 'search.html', context)


def generate_report(request):
    results = None

    if request.method == 'GET':
        # Get the search criteria from the request parameters
        report_type = request.GET.get('report_type')
        month = request.GET.get('month')
        year = request.GET.get('year')

        # Filter the results based on the report type
        if report_type == 'property_type':
            results = Search.objects.filter(
                date__month=month,
                date__year=year,
                property_type_id__isnull=False
            ).values('property_type__property_type_name').annotate(count=Count('id'))
        elif report_type == 'neighborhood_type':
            results = Search.objects.filter(
                date__month=month,
                date__year=year,
                property_neighborhood__id__isnull=False
            ).values('property_neighborhood__property_neighborhood_name').annotate(count=Count('id'))
        elif report_type == 'price_range_type':
            results = Search.objects.filter(
                date__month=month,
                date__year=year,
                property_type_price_range_id__isnull=False
            ).values('property_type_price_range__property_price_range_name').annotate(count=Count('id'))


    return render(request, 'report.html', {'results': results})


def enquire_view(request):
    return render(request, 'enquire.html')


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

def remove_listing(request, property_id):
    property = Property.objects.get(id=property_id)
    property.flag = False
    property.save()
    return redirect('home:listings')