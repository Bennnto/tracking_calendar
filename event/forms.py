from django import forms
from .models import MyEvent


class EventForm(forms.ModelForm):
    class Meta :
        model = MyEvent
        fields = ["title", "description", "location", "date", "start_time", "end_time"]
        widgets = {
            "title" : forms.TextInput(attrs={"class": "form-title"}),
            "description" : forms.Textarea(attrs={"class": "form-description"}),
            "location": forms.TextInput(attrs={"class": "form-location"}),
            "date": forms.DateInput(
                attrs={"type": "date", "class": "form-date"}
            ),
            "start_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-time"}
            ),
            "end_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-time"}
            ),
        }