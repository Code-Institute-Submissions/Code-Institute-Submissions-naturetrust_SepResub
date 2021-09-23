from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def user_orders(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/user-orders.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def profile_games(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile-games.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def profile_adoptions(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile-adoptions.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)
