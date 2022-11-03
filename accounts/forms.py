from django import forms
from .models import Account

class SingupForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(SingupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mt-2'
