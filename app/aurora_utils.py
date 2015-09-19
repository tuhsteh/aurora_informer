import json
import urllib2
from lxml import html
import requests 

page = requests.get('http://www.spaceweatherlive.com/en/auroral-activity/kp')
tree = html.fromstring(page.text)


################################
#
# This function identifies a persons geographic latitude from a zip code
# 
################################
# NOTE: We will need to find a way to convert this to geomagnetic latitude for the program to work.
#
#
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


################################
#
# This function identifies percentage chance of visibility by latitude range
#
################################
# According to: http://www.spaceweatherlive.com/en/help/the-low-middle-and-high-latitude
# High Latitude = 60 degrees (magnetic lat) or higher
# Middle Latitude = 50 to 60 degrees (magnetic lat)
#
#


def get_aurora_chance(by_lat): #Pass in one of the by_lat options to get a percent chance response by latitude
    if by_lat == "kp_max":
        predicted_kp_max = tree.xpath('//td[text()="Predicted Kp max"]/following-sibling::td[1]/text()')
        return predicted_kp_max[0]
    elif by_lat == "high_lat":
        high_lat_chance = tree.xpath('//td[text()="High latitude"]/following-sibling::td[1]/span/text()')
        return high_lat_chance[0]
    elif by_lat == "middle_lat":
        middle_lat_chance = tree.xpath('//td[text()="Middle latitude"]/following-sibling::td[1]/span/text()')
        return middle_lat_chance[0]
    elif by_lat == "low_lat":
        low_lat_chance = tree.xpath('//td[text()="Low latitude"]/following-sibling::td[1]/span/text()')
        return low_lat_chance[0]