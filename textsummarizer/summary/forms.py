from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class textForm(forms.Form):
    _type = forms.CharField(label="Choose type of summarization:", widget=forms.Select(choices=[("Abstractive", "Abstractive"), ("Extractive", "Extractive")]))
    text = forms.CharField(label='Enter text to summarize:', empty_value = "", required=False, widget=forms.Textarea)
    file = forms.FileField(required=False)
    percent = forms.IntegerField(label="Enter summary percentage:", initial = 20, validators=[MinValueValidator(0),MaxValueValidator(100)])
    
    def clean(self):
        text = self.cleaned_data.get('text')
        file = self.cleaned_data.get('file')
        if not text and not file:
            raise forms.ValidationError('Either add some text or upload a file.')
        return self.cleaned_data