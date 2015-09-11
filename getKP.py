from lxml import html
import requests
import re

page = requests.get('http://www.spaceweatherlive.com/en/auroral-activity/kp')
tree = html.fromstring(page.text)

predicted_kp_max = tree.xpath('//td[text()="Predicted Kp max"]/following-sibling::td[1]/text()')
high_lat_chance = tree.xpath('//td[text()="High latitude"]/following-sibling::td[1]/span/text()')
middle_lat_chance = tree.xpath('//td[text()="Middle latitude"]/following-sibling::td[1]/span/text()')
low_lat_chance = tree.xpath('//td[text()="Low latitude"]/following-sibling::td[1]/span/text()')

print "%24s:\t%s" % ("High Latitude Chance", high_lat_chance[0])
print "%24s:\t%s" % ("Mid Latitude Chance", middle_lat_chance[0])
print "%24s:\t%s" % ("Low Latitude Chance", low_lat_chance[0])
print "%24s:\t%s" % ("Predicted KP Max", predicted_kp_max[0])

#Function to clean up results#

def rip_percent(lat):
    lat_no_percent = lat.replace("%", "")
    print lat_no_percent

#rip_percent(middle_lat_chance[0])

