from .models import Badge, BadgeCategory, Dashboard
from books.models import BookShelf

def award_possible_badge(category: BadgeCategory, dashboard: Dashboard, points: int) -> int:
    '''
    Given a specified category, award all badges based on the number of points earned.
    Must verify that points are positive. Badges won't be removed.
    Returns the change in the number of badges awarded
    '''
 
    sorted_badges = Badge.objects.filter(category = category).order_by('points_required')
    previously_awarded_badges = dashboard.badges.count
    # print(f"Sorted Badges: {sorted_badges}")
    for badge in sorted_badges:
        if points >= badge.points_required:
            badge.add_badge(dashboard)
            # print(f"Badge: {badge} added to {dashboard.user.username}'s dashboard")
        # print(f"Badge: {badge}, Points Required: {badge.points_required}")

    currently_awarded_badges = dashboard.badges.count
    newly_awarded_badges = currently_awarded_badges = previously_awarded_badges
    return newly_awarded_badges

def get_pages_read(dashboard: Dashboard) -> int:
    read_shelf = BookShelf.objects.filter(shelved_by = dashboard.user).filter(shelf = 'read')
    books_read = list(shelf.book for shelf in read_shelf)
    pages_read = 0
    for book in books_read:
        pages_read += book.pages
    return pages_read
