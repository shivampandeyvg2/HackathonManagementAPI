from django import forms
from django.forms import ModelForm
from .models import Hackathon


class HackathonDetailForm(ModelForm):
    class Meta:
        model = Hackathon
        fields = "__all__"

