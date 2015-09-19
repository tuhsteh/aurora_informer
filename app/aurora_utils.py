import json
import urllib2

def get_latitude(user_zip):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=true" % user_zip
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    northeast_lat = data["results"][0]["geometry"]["bounds"]["northeast"]["lat"]
    southwest_lat = data["results"][0]["geometry"]["bounds"]["southwest"]["lat"]
    print "northeast latitude: %s" % northeast_lat
    print "southwest latitude: %s" % southwest_lat
    return northeast_lat
    #print float(int(northeast_lat) + int(southwest_lat)) / (2) #The math for the average isn't quite right.
