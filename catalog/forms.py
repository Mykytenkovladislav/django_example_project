import datetime

from catalog.models import Person

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import pytz

User = get_user_model()


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ContactFrom(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class TriangleCalculationForm(forms.Form):
    leg_a = forms.IntegerField(required=True, min_value=1, max_value=1000)
    leg_b = forms.IntegerField(required=True, min_value=1, max_value=1000)


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email']


class SendEmailForm(forms.Form):
    email = forms.EmailField(required=True)
    reminder = forms.CharField(widget=forms.Textarea, required=True)
    date_and_time = forms.DateTimeField(required=True, input_formats=['2006-10-25 14:30'],
                                        initial=datetime.datetime.now)

    def clean_date_and_time(self):
        data = self.cleaned_data['date_and_time']

        utc = pytz.UTC

        # Check date is not in past.
        if data < utc.localize(datetime.datetime.today()):
            raise forms.ValidationError(_('Invalid date - reminder send date in past'))
        # Check date is in range librarian allowed to change (+2 days)
        if data > utc.localize(datetime.datetime.today()) + datetime.timedelta(days=2):
            raise forms.ValidationError(_('Invalid date - reminder send date is  more than 2 days ahead'))

        return data
