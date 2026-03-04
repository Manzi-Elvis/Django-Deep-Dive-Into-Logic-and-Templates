from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }