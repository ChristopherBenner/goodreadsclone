from django.contrib.auth.models import User
from django.test import TestCase
from .models import Badge, BadgeCategory, Dashboard

from .functions import award_possible_badge

class BadgeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test_user', password = 'test_password')
        self.user_dashboard = Dashboard.objects.create(user = self.user)
        self.category = BadgeCategory.objects.create(name='category1')
        self.badge1 = Badge.objects.create(name='badge1', description='The first badge', category = self.category, points_required = 15)
        self.badge2 = Badge.objects.create(name='badge2', description='The second badge', category = self.category, points_required = 30)
        self.badge1.save()
        self.badge2.save()
        self.user_dashboard.save()

    def test_list_badges(self):
        print('test list badges')
        self.user_dashboard.badges.add(self.badge1)
        self.assertIn(self.badge1, self.user_dashboard.list_badges())

    def test_list_badges_multiple_false(self):
        print('test list badges multiple = False')
        print(f"Self.category: {self.category}")
        self.user_dashboard.badges.add(self.badge1)
        self.user_dashboard.badges.add(self.badge2)

        self.assertNotIn(self.badge1, self.user_dashboard.list_badges(False))
        self.assertIn(self.badge2, self.user_dashboard.list_badges(False))

    
    def test_add_badge(self):
        print('test add badge')
        self.badge1.add_badge(self.user_dashboard)
        self.assertIn(self.badge1, self.user_dashboard.list_badges())

    def test_add_two_badges(self):
        print('test add two badges')
        self.badge1.add_badge(self.user_dashboard)
        self.badge2.add_badge(self.user_dashboard)
                
        self.assertIn(self.badge1, self.user_dashboard.list_badges())
        self.assertIn(self.badge2, self.user_dashboard.list_badges())
 
    def test_award_possible_badge_low(self):
        print('test award add possible badge low')
        award_possible_badge(self.category, self.user_dashboard, 0)
        
        self.assertEquals(self.user_dashboard.list_badges(), [])

    def test_award_possible_badge_one(self):
        print('test award possible badge one')
        award_possible_badge(self.category, self.user_dashboard, 20)

        self.assertNotIn(self.badge2, self.user_dashboard.list_badges())
        self.assertIn(self.badge1, self.user_dashboard.list_badges() )

    def test_award_possible_badge_two(self):
        print('test award possible badge two')
        award_possible_badge(self.category, self.user_dashboard, 45)

        self.assertIn(self.badge1, self.user_dashboard.list_badges())
        self.assertIn(self.badge2, self.user_dashboard.list_badges())
