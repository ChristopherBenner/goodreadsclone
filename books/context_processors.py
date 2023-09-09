from dashboard.models import Dashboard
def badge_processor(request):
    if request.user.is_authenticated:
        # dashboard = request.user.dashboard
        dashboard = Dashboard.objects.filter(user = request.user).first()
        num_badges = dashboard.badges.count
    else:
        num_badges = 0

    return {'num_badges' : num_badges}