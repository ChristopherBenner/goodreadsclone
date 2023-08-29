from django import forms
from .models import Commment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            })
        }