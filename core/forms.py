from django import forms
from core.tasks import send_feedback_email_task

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 5}))
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        # " try to trick spammers by checking whether the honeypot field is
        # filled in; not supper complicated/effective but it works"
        if self.cleaned_data['honeyport']:
            return False
        send_feedback_email_task.delay(
            self.cleaned_data['email'], self.cleaned_data['message']
        )