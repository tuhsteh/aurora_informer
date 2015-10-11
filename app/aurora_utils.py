import json
import urllib2
from aacgmv2 import convert
import datetime
import time



from lxml import html


#import requests 

#page = urllib2.urlopen('http://www.spaceweatherlive.com/en/auroral-activity/kp')
page = urllib2.urlopen('http://www.spaceweatherlive.com/en/auroral-activity/')
#tree = html.fromstring(page.text)

#Snag API Key
with open ("no_track_api_key", "r") as mfile:
    apiKey=mfile.read().replace('\n', '')

################################
#
# This function identifies a persons geographic latitude from a zip code
# 
################################
# NOTE: We will need to find a way to convert this to geomagnetic latitude for the program to work.
#
#
def get_geo_coords(user_zip):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=true" % user_zip
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    geographic_latitude = data["results"][0]["geometry"]["location"]["lat"]
    geographic_longitude = data["results"][0]["geometry"]["location"]["lng"]
    lats = [geographic_latitude, geographic_longitude]                          
    
    return lats

def get_elevation(lat, lon):
    url = "https://maps.googleapis.com/maps/api/elevation/json?locations=%s,%s&key=%s" % (lat, lon, apiKey)
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    altitude = data["results"][0]["elevation"]
    inMeters = altitude / float(1000)
    return inMeters

def geo2mag(lat, lon, alt):
    #Latitudes range from -90 to 90.
    #Longitudes range from -180 to 180. (Maybe, who knows --  http://ccmc.gsfc.nasa.gov/requests/instant/ranges.php
    #Verified with http://ccmc.gsfc.nasa.gov/requests/instant/instant1.php?model=AACGM&type=1
    mlat, mlon = convert(lat, lon, alt, None)
    return mlat
    # Eagle ID
    # Lat - 43.77369
    # Lon - -116.3805805
    # Alt - 1
    #Decent match to http://wdc.kugi.kyoto-u.ac.jp/cgi-bin/trans-cgi
    
#geo2mag(60, 15, 300)

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
    
#get_aurora_chance("high_lat")