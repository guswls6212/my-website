from django.db import models
from django import forms
from django.forms import ModelForm
from leeblog.models import Maker, Label


class MakerForm(forms.ModelForm):

    class Meta:
        model = Maker
        fields ='__all__'

class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields =[
                    # 'maker',
                    'sw_version',
                    'os_version',
                    'label_file'
        ]
