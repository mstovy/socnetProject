# socnetProject

Proposition:


Use Gowalla data and find all communties using networkx code

Select the tightest knit communiteis (most dense? shortest paths?)

Display the general (avg?) location of the communites to a US map i

Overlay an existing map (find a basemap? maybe look for something that already exist that we can adapt the data to)of the areas where the population is of low socio-econimc status

Write the graph to an HTML doc that can be displayed in browser simply

Include a breif description of our hypothesis & an analysis of how our results came out



  issue 1 - how to display the networkx graph
  
  issue 2 - how do we overlay a graph onto the networkx graph
  
  issue 3 - how will we determine what constitutes a tightly knit community


resources:

could implement something like [this](https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db) but using networkx instead of matlab

looks as if we may have to use matlab to use a base map to plot onto.
[here](https://sensitivecities.com/so-youd-like-to-make-a-map-using-python-EN.html#.X6R5wy2ZNAY) are [some](https://stackoverflow.com/questions/19915266/drawing-a-graph-with-networkx-on-a-basemap) examples of how we can plot our data using coordinates and matlab. May just need to use networkx as a form of reading in the data and finding communities.

the [mplleaflet](https://github.com/jwass/mplleaflet) library seems like it could be utilized sinze we are using coordinates.
