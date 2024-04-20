from django import forms
from crudApp.models import student
# Create your models here.
class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

