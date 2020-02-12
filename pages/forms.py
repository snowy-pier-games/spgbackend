from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class SubscribeForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
