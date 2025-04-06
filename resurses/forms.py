from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from resurses.models import Counters

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CountersForm(forms.ModelForm):
    class Meta:
        model = Counters
        fields = '__all__'
        labels = {
            'year': 'Год',
            'month': 'Месяц',
            'elec_day': 'Электричество День',
            'elec_night': 'Электричество Ночь',
            'water': 'Холодная вода',
            'gas': 'Газ',
        }
    def __init__(self, *args, **kwargs):
        super(CountersForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-label'})
