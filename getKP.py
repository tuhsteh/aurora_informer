from lxml import html
import requests

page = requests.get('http://www.spaceweatherlive.com/en/auroral-activity/kp')
tree = html.fromstring(page.text)

predicted_kp_max = ""
high_lat_chance = ""
middle_lat_chance = ""
low_lat_chance = ""

latitude_options = ['high', 'middle', 'low', 'kp_max', 'exit']

selectionIs = "--------------\n"
selectionIs += "Your options:\n"
selectionIs += "--------------\n"
selectionIs += "kp_max\n"
selectionIs += "high_lat\n"
selectionIs += "middle_lat\n"
selectionIs += "low_lat\n"

def get_aurora_chance(by_lat):
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
    #print "%24s:\t%s" % ("High Latitude Chance", high_lat_chance[0])
    #print "%24s:\t%s" % ("Mid Latitude Chance", middle_lat_chance[0])
    #print "%24s:\t%s" % ("Low Latitude Chance", low_lat_chance[0])
    #print "%24s:\t%s" % ("Predicted KP Max", predicted_kp_max[0])


#########################
#
# Function to rip the percentage out, I plan on using this later for notifying based on probability.
#
#########################
def rip_percent(lat):
    lat_no_percent = lat.replace("%", "")
    print lat_no_percent

def handle_it(choices):
    if "high" in choices:
        my_answer = get_aurora_chance("high_lat")
        print(my_answer)
    elif "middle" in choices:
        my_answer = get_aurora_chance("middle_lat")
        print(my_answer)
    elif "low" in choices:
        my_answer = get_aurora_chance("low_lat")
        print(my_answer)
    else:
        my_answer = get_aurora_chance("kp_max")
        print(my_answer)


def main():
    print selectionIs
    mychoice = raw_input("What would you like to know?\n")
    if mychoice in latitude_options:
        handle_it(mychoice)
    else: 
        print "Invalid selection, please try again"
        main()
    

main()
#blah = get_aurora_chance("kp_max")
#print blah





