import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
import re
import plotly.express as px

# read data from file
data = pd.read_csv('DataWeierstrass.csv', delimiter = ';')
# group by professor and lecture name and get the mean value
grouped = data.groupby(['professor', 'lecture'], as_index=False).mean()
text=[grouped.loc[ i, 'professor'] for i in range(len(grouped))]

professors = grouped['professor'].drop_duplicates()

profColor ={professors.values[i]: i for i in range(len(professors))}

color_vals=[profColor[c] for c in grouped['professor']]
#build the the scatterplot matrix
result = go.Splom(dimensions=[dict(label='Lecture',
                                 values=grouped['lecture']),
                            dict(label='Participants',
                                 values=grouped['participants']),
                            dict(label='Expertise',
                                 values=grouped['professional expertise']),
                            dict(label='Motivetion',
                                 values=grouped['motivation']),
                            dict(label='Presentation',
                                 values=grouped['clear presentation']),
                            dict(label='Impression',
                                 values=grouped['overall impression'])],

                text=text,
                marker=dict(color=color_vals,
                            size=6,
                            colorscale= 'Jet',
                            showscale=True,
                            line=dict(width=0.5,
                                      color='rgb(230,230,230)'),
							colorbar= dict(title ='Professor'))
                )

result['diagonal'].update(visible=False)# make the diagonal of the matrix invisible	

layout = go.Layout(width=1400,height=800,
    title=go.layout.Title(
        text='Scatterplot matrix'
    ))
fig1 = dict(data=[result], layout = layout)
py.plot(fig1, filename =  "scatterplot matrix"+".html")


#converting lecture names to lecture numbers
lectureNumbers = []
for i in range(101):
    str1 = grouped['lecture'].values[i]
    lectureNumbers.append(int(re.findall('\d+', str(str1))[0]))
#build the parallel coorindates plots

layout2 = go.Layout(width=1400,height=800,
    title=go.layout.Title(
        text='Parallel Coordinates.'
    ))

pc_data = [
    go.Parcoords(
        line = dict(color = grouped['professor'].values,  colorscale = 'Jet',showscale = True, reversescale=True, colorbar= dict(title ='Professor')),
		name = 'professor',
		visible = True,
        dimensions = list([
            dict(label = 'professor', values = grouped['professor'].values),
            dict(label = 'lecture', values = grouped['lecture'].values),
            dict(label = 'participants', values = grouped['participants'].values),
            dict(label = 'professional expertise', values = grouped['professional expertise'].values, range = [1,5]),
            dict(label = 'motivation', values = grouped['motivation'].values, range = [1,5]),
            dict(label = 'clear presentation', values = grouped['clear presentation'].values, range = [1,5]),
            dict(label = 'overall impression', values = grouped['overall impression'].values, range = [1,5]),
        ])
    )
]
fig2 = go.Figure(data = pc_data, layout = layout2)
py.offline.plot(fig2,filename =  "parallel coordinates"+".html")

