from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.fields[field].required:
                label = f'{field} *'
                self.fields[field].label = label
            else:
                label = f'{field}'
                self.fields[field].label = label
