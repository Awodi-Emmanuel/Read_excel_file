from tkinter import Widget
from django import forms 

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Addres")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'row': 5})
    )
    honeypot = forms.CharField(Widget=forms.HiddenInput(), required=False)