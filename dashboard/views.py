from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import BadgeCategory, Badge, Dashboard

from .functions import award_possible_badge # remove after testing
# Create your views here.
@login_required
def display_badges(request):
    '''
    Display which badges have been earned by the user.
    If list_badges(True) -> Display all earned badges
    If list_badges(False) -> Display only the highest badge of a category
    '''
    categories = BadgeCategory.objects.all()
    badges = Badge.objects.all()

    user_dashboard = Dashboard.objects.filter(user = request.user)[0]
    '''badge_names = list(badge.id for badge in badges)
    user_dashboard.badges.remove(badge_names[0])''' # Use this as necessary to remove all badges for testing
    list_of_badges, badges_to_display = user_dashboard.list_badges(True) 
    
    
    return render(request, 'dashboard/display_badges.html', {
        'categories': categories,
        'badges': badges,
        'list_of_badges': list_of_badges,
        'badges_to_display': badges_to_display,
    } )