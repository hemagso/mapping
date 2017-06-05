import gmplot
from bs4 import BeautifulSoup

def insertapikey(fname, apikey):
    """put the google api key in a html file"""
    def putkey(htmltxt, apikey, apistring=None):
        """put the apikey in the htmltxt and return soup"""
        if not apistring:
            apistring = "https://maps.googleapis.com/maps/api/js?key=%s&callback=initMap"
        soup = BeautifulSoup(htmltxt, 'html.parser')
        body = soup.body
        src = apistring % (apikey, )
        tscript = soup.new_tag("script", src=src, async="defer")
        body.insert(-1, tscript)
        return soup
    htmltxt = open(fname, 'r').read()
    soup = putkey(htmltxt, apikey)
    newtxt = soup.prettify()
    open(fname, 'w').write(newtxt)

def plot_region(region,points,output="maps/map.html"):
    x_coords, y_coords = tuple(shapely.geometry.shape(shape).exterior.coords.xy)
    border_utm = zip(x_coords, y_coords)    
    border_geo = map(
        lambda point: utm.to_latlon(point[0], point[1],UTM_REGION_1,UTM_REGION_2),
        border_utm
    )
    border_lat, border_long = zip(*border_geo)
    points_lat, points_long = zip(*points)

    gmap = gmplot.GoogleMapPlotter(list_lat[0], list_long[0], 16)
    gmap.plot(border_lat, border_long, 'cornflowerblue', edge_width=10)
    gmap.scatter(list_lat, list_long, '#3B0B39', size=40, marker=False)
    gmap.draw(output)
    insertapikey("maps/map01.html", apikey)
    
plot_region(shape,points_geo)