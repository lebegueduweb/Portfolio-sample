from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
import datetime
from django import forms

#the form allowing users to renew book and function to get  a new date
class RenewBookForm(forms.Form):
    RenewalDate = forms.DateField(help_text= 'Enter a date between now and 4weeks (default3).')
    def overwriteRenewalDate(self):
        data = self.cleaned_data['RenewalDate']
        #Make sure Date is not in past
        if data < datetime.date.today():
            raise ValidationError(-('Your renewal date is in the past'))

        #check date is in range librarian allowed to change
        if data > datetime.date.today() + datetime.timedelta(week=4):
            raise ValidationError(_('Your renewal date exceeds 4 weeks'))

        #Cleaned data must always be returned
        return data