from django import forms
from .models import Commment, BookShelf

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            })
        }

SHELF_CHOICES = [
    ('want to read', 'Want to Read'),
    ('currently reading', 'Currently Reading'),
    ('read', 'Read'),
]

class ShelvingForm(forms.ModelForm):
    
    shelf = forms.CharField(widget=forms.Select(choices=SHELF_CHOICES))
    class Meta:
        model = BookShelf
        fields = ('shelf',)