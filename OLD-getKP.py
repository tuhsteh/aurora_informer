from lxml import html
import requests
import smtplib

page = requests.get('http://www.spaceweatherlive.com/en/auroral-activity/')
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
        print predicted_kp_max[0]
    elif by_lat == "high_lat":
        high_lat_chance = tree.xpath('//td[text()="High latitude"]/following-sibling::td[1]/span/text()')
        print high_lat_chance[0]
    elif by_lat == "middle_lat":
        middle_lat_chance = tree.xpath('//td[text()="Middle latitude"]/following-sibling::td[1]/span/text()')
        print middle_lat_chance[0]
    elif by_lat == "low_lat":
        low_lat_chance = tree.xpath('//td[text()="Low latitude"]/following-sibling::td[1]/span/text()')
        print low_lat_chance[0]
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


#########################
#
# Figures out what you chose.
#
#########################
def handle_it(choices):
    if "high" in choices:
        my_answer = get_aurora_chance("high_lat")
        print(my_answer)
        yield(my_answer)
    elif "middle" in choices:
        my_answer = get_aurora_chance("middle_lat")
        print(my_answer)
        yield(my_answer)
    elif "low" in choices:
        my_answer = get_aurora_chance("low_lat")
        #print(my_answer).
        yield(my_answer)
    else:
        my_answer = get_aurora_chance("kp_max")
        #print(my_answer)
        yield(my_answer)
    ask_subscribe()


#########################
#
# See if people would like to subscribe.
#
#########################
def ask_subscribe():
    maybe = raw_input("Would you to receive updates on aruroa borealis visibility? (y/n)\n")
    if "y" in maybe:
        #print "OK we will subscribe you."
        act_scubscribe()
    elif "n" in maybe:
        print "okay, exiting..."
    else:
        print "Invalid selection.\n"
        ask_subscribe()
        
 #########################
#
# Subscribe & Email - Will doll this up later to store info in a datbase..
#
#########################       

def act_scubscribe():
    sender = "aurora_updates@aurora-informer.com"
    receivers = raw_input("what is your e-mail address?")
    mylat = raw_input("What latitude would you like updates on?")
    mynotif = handle_it(mylat)
    message = """From: From Person <from@fromdomain.com>
                To: To Person <to@todomain.com>
                Subject: SMTP e-mail test
                
                Aurora Borealis visibility: %s
                """ % mynotif
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print "Successfully sent email"
    except:
        print "Error: unable to send email"
#########################
#
# Kick off the program.
#
#########################

def main():
    print selectionIs
    mychoice = raw_input("What would you like to know?\n")
    if mychoice in latitude_options:
        handle_it(mychoice)
    else: 
        print "Invalid selection, please try again\n"
        main()
    

#main()

#main()
get_aurora_chance("middle_lat")






