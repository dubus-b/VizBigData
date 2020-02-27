from django.shortcuts import render
from django.template.response import TemplateResponse
import plotly.graph_objects as go
import numpy as np
import plotly.offline as opy
import plotly.express as px


import pandas as pd

#fig = go.Figure(data=go.Scatter(x=data['math score'], y=data['reading score'], mode='markers', marker_color=data['gender']))

# Create your views here.

def index(request):
    # Nous utilisons pandas pour faciliter la lecture des données du csv
    data = pd.read_csv('data.csv')
    figo = px.scatter(data, x="math score", y="reading score", color="lunch",
                 hover_data=['lunch'])
    div = opy.plot(figo, output_type='div')
    return TemplateResponse(request, 'index.html', {'data' : div})