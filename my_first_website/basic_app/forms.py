from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        # بنحدد الحقول اللي عايزينها تظهر في الفورم
        fields = ['name', 'email', 'subject', 'message']

        # الـ widgets بتسمح لنا نضيف Bootstrap Classes عشان الشكل يفضل جميل
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your message here...'}),
        }