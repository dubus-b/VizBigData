from django.shortcuts import render
from django.template.response import TemplateResponse
import plotly.graph_objects as go
import numpy as np


import pandas as pd


# Create your views here.

def index(request):
    # Nous utilisons pandas pour faciliter la lecture des données du csv
    data = pd.read_csv('data.csv')
    print(data['math score'])
    fig = go.Figure(data=go.Scatter(x=data['math score'], y=data['reading score'], mode='markers'), color=data['gender'])
    fig.show()    
    return TemplateResponse(request, 'index.html', {'data' : data})