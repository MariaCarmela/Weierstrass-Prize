# Weierstrass-Prize
The task is to find candidates for the Weierstrass-Prize (“Best Teacher”). To decide which professor is worth considering for the award the following characteristics are checked: professor, lecture, number of participants visiting lecture, professional expertise, motivation, clear presentation and overall impression. Scatter plot graph and parallel coordinates graph are used to visualize the data and to help the search.

The  visualizations are made with [Plotly](https://plotly.com/python/), a Python graphing library that makes interactive, publication-quality graphs.
The graphs used for this project(the scatter plot and parallel coordinates graphs) let the user interact with navigating, selecting, filtering in this way:
* *passing* throw the graph (using the mouse) to read the values for each feature
* *zooming* in and out (scrolling with mouse) to see data more clearly and to focus the attention on specific parts of the graphs.
* *clicking* (mouse event) to highlight specific value of each feature

The main modules used are the following:
* *[plotly.express]*(https://plotly.com/python/plotly-express/) that contains functions that can create entire figures at once
* *plotly.offline*
* *plotly.graph_objs*  that creates [Graph Objects](https://plotly.com/python/graph-objects/)
