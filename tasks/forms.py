from django.forms import ModelForm
from django.forms.widgets import DateInput, TimeInput
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['date', 'title', 'starttime', 'endtime']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'starttime': TimeInput(attrs={'type': 'time'}),
            'endtime': TimeInput(attrs={'type': 'time'})
        }