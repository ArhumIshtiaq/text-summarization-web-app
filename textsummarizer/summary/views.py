from django.shortcuts import render
from .forms import textForm, UploadFileForm
from .preprocessing import *
from .summarize import *
from nltk.tokenize import sent_tokenize
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


def index(request):
    if request.method == 'POST':
        form = textForm(request.POST)
        if form.is_valid():
            _type = form.cleaned_data['_type']
            text = form.cleaned_data['text']
            percent = form.cleaned_data['percent']
            tokenized_sentence = sent_tokenize(text)
            if (_type == 'Extractive'):
                summary = summarize(tokenized_sentence, percent)
                return render(request, 'summary/summary.html', {'text': text, 'summary': summary, 'percent': "Not Applicable"})
            elif (_type == 'Abstractive'):
                model_name = 'google/pegasus-xsum'
                torch_device = 'cuda'
                tokenizer = PegasusTokenizer.from_pretrained(model_name)
                model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
                batch = tokenizer.prepare_seq2seq_batch([text], truncation=True, padding='longest').to(torch_device)
                translated = model.generate(**batch)
                summary = tokenizer.batch_decode(translated, skip_special_tokens=True)
                return render(request, 'summary/summary.html', {'text': text, 'summary': summary[0], 'percent': "Not Applicable"})
    else:
        form = textForm()
    return render(request, 'summary/index.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("here before done \n")
            text = request.FILES['file'].read()
            print(text)
            print("here done \n")
            percent = form.cleaned_data['percent']
            if (_type == 'Extractive'):
                summary = summarize(tokenized_sentence, percent)
                return render(request, 'summary/summary.html', {'text': text, 'summary': summary, 'percent': "Not Applicable"})
            elif (_type == 'Abstractive'):
                model_name = 'google/pegasus-xsum'
                torch_device = 'cuda'
                tokenizer = PegasusTokenizer.from_pretrained(model_name)
                model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
                batch = tokenizer.prepare_seq2seq_batch([text], truncation=True, padding='longest').to(torch_device)
                translated = model.generate(**batch)
                summary = tokenizer.batch_decode(translated, skip_special_tokens=True)
                return render(request, 'summary/summary.html', {'text': text, 'summary': summary[0], 'percent': "Not Applicable"})
    else:
        form = UploadFileForm()
    return render(request, 'summary/index.html', {'form': form})