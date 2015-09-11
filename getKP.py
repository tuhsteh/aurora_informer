from lxml import html
import requests
import re

page = requests.get('http://www.spaceweatherlive.com/en/auroral-activity/kp')
tree = html.fromstring(page.text)

predicted_kp_max = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/table[2]/tbody/tr[3]/td[2]/text()')
high_lat_chance = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/table[1]/tbody/tr[1]/td[2]/span/text()')
middle_lat_chance = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/table[1]/tbody/tr[2]/td[2]/span/text()')
low_lat_chance = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/table[1]/tbody/tr[3]/td[2]/span/text()')

print "High Lattitude Chance: ", high_lat_chance[0]
print "Mid Lattitude Chance: ", middle_lat_chance[0]
print "Low Lattitude Chance: ", low_lat_chance[0]
print "Predicted KP Max: ", predicted_kp_max[0]

#Function to clean up results#

def rip_percent(lat):
    lat_no_percent = lat.replace("%", "")
    print lat_no_percent

#rip_percent(middle_lat_chance[0])

