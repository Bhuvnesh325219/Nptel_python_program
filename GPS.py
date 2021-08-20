
import csv

from gmplot import gmplot

gmap =gmplot.GoogleMapPlotter(28.689169,77,324448)


#gmap.coloricon="https://www.googlemapsmarkers.com/v1/%s/"

lat=28.689169
long=77,324448

gmap.marker(lat,long,'yellow')

gmap.draw("mymap.html")
