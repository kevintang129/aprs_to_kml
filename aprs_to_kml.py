# generates a kml file from aprs data from a csv with columns 
# name, description, latitude, longitude, and altitude

import csv, simplekml

def generate_point(title, desc, lat, lon, alt):
    pnt = kml.newpoint(name=title, description = desc, coords=[(lon, lat, alt)])
    pnt.altitudemode = simplekml.AltitudeMode.absolute
    pnt.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
    pnt.style = style

kml = simplekml.Kml()
style = simplekml.Style()
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png'

with open('balloon_position.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    line_coords = []
    for row in reader:
        generate_point(row[1], row[2], float(row[3]), float(row[4]), float(row[5]))
        line_coords += [(float(row[4]), float(row[3]), float(row[5]))]

    ls = kml.newlinestring(name='HAB_flight')
    ls.coords = line_coords
    ls.altitudemode = simplekml.AltitudeMode.absolute

    kml.save("HAB_path.kml")
