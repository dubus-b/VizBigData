from django.shortcuts import render
from django.template.response import TemplateResponse
import plotly.graph_objects as go
import numpy as np
import plotly.offline as opy
import plotly.express as px
import pandas as pd
import plotly.express as px
import plotly as py

data = pd.read_csv('data.csv')


def get_pie_chart():
    fig = px.pie(data, values='reading score', names='race/ethnicity', title='race/ethnicity')
    return opy.plot(fig, output_type='div')

    #fig = go.Figure(data=go.Scatter(x=data['math score'], y=data['reading score'], mode='markers', marker_color=data['gender']))

    # Create your views here.
#labels={'sexe':data["gender"], 'Writing': "writing score", 'Reading': "reading score", 'Math': "math score",}

def index(request):
    # Nous utilisons pandas pour faciliter la lecture des données du csv
    figo = px.scatter(data, x="reading score", y="writing score", color="race/ethnicity",
                      hover_data=['gender'])
    figo.update_layout(title='',
                       yaxis_zeroline=False, xaxis_zeroline=False)
    div = opy.plot(figo, output_type='div')

    figu = px.parallel_coordinates(data, dimensions=["gender", "writing score", "reading score", "math score"],
                        color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
    div2 = opy.plot(figu, output_type='div')

    return TemplateResponse(request, 'index.html', {'data' : div, 'data2': div2, 'pie' : get_pie_chart()})
