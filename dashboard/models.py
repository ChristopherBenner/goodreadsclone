from django.contrib.auth.models import User
from django.db import models

class BadgeCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Badge Categories'

    def __str__(self) -> str:
        return self.name

class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(BadgeCategory, related_name='category', on_delete=models.CASCADE, null=True, blank=True)
    points_required = models.IntegerField(default=0)
    awarded_image = models.ImageField(upload_to='badge_images/', null=True, blank=True)
    not_awarded_image = models.ImageField(upload_to='badge_images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def add_badge(self, dashboard):
        dashboard.badges.add(self)

class Dashboard(models.Model):
    user = models.ForeignKey(User, related_name='dashboard', on_delete=models.CASCADE)
    badges = models.ManyToManyField(Badge, related_name='badges')
    pages_read = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.user.username
    
    def list_badges(self, multiple_allowed = True) -> list:
        '''
        Return a list of all badges assigned. If multiple are allowed, 
        List every badge earned. If not, only list the highest badge of
        each category earned.
        '''
        badges_to_display = []
        categories = BadgeCategory.objects.all()
        list_of_badges = list(self.badges.all())

        if not multiple_allowed:
            for category in categories:
                sorted_badges = Badge.objects.filter(category = category).order_by('-points_required')
                # print(f"Sorted Badges: {sorted_badges}")
                for badge in sorted_badges:
                    if badge in list_of_badges:
                        badges_to_display.append(badge)
                        break
        else:
            badges_to_display = list_of_badges
            
    
        print(f"List of badges: {list_of_badges}, Badges to Display: {badges_to_display}")
        return list_of_badges, badges_to_display
    
    def add_badge(self, badge):
        '''
        Easily add a badge to badges assigned. Duplicates prevented with ManyToMany field. 
        Additional code to test this is not necessary.
        '''
        self.badges.add(badge)