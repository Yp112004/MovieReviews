from django.forms import ModelForm, Textarea
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Use super() correctly
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})
    
    class Meta:
        model = Review
        fields = ['text', 'watchAgain']  # Ensure 'watchAgain' is included
        labels = {
            'watchAgain': 'Watch Again'
        }
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }