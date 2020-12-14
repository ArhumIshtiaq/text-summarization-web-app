from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class textForm(forms.Form):
    _type = forms.CharField(label="Choose type of summarization:", widget=forms.Select(choices=[("Abstractive", "Abstractive"), ("Extractive", "Extractive")]))
    text = forms.CharField(label='Enter text to summarize:', widget=forms.Textarea)
    percent = forms.IntegerField(label="Enter summary percentage:", validators=[MinValueValidator(0),MaxValueValidator(100)])