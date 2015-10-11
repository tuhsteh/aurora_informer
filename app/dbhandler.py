import sqlite3 as lite
import sys
from email import email
import os


#
# Not creating the schema properly.
#
#def create_db():
#    con = lite.connect('aurora_db.db')
#    with con:
#        cur = con.cursor()    
#        cur.execute("CREATE TABLE Subscribers(Id INTEGER PRIMARY KEY, Name TEXT, Email TEXT, Geographic_Lat INT, Geographic_Lon INT, Altitude_km INT, Geomagnetic_Lat INT, Geomagnetic_Lon INT, Threshold INT, Pin INT);")

def createSimpleDB():
    con = lite.connect('aurora_simple.db')
    with con:
        cur = con.cursor()
        #cur.execute("CREATE TABLE Subscribers(Name TEXT, Email TEXT);")
        cur.execute("CREATE TABLE Subscribers(Id INTEGER PRIMARY KEY, Name TEXT, Email TEXT, Geographic_Lat TEXT, Geographic_Lon TEXT, Altitude TEXT, Geomagnetic_Lat TEXT, Zip TEXT);")

def create_user(name, email, geo_lat, geo_lon, altitude, geomagnetic_lat, zip):
    os.chdir("/home/john/code/aurora_informer/app")
    con = lite.connect('aurora_simple.db')
    insertStatement = (name, email)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Subscribers ('Name', 'Email', 'Geographic_Lat', 'Geographic_Lon', 'Altitude', 'Geomagnetic_lat', 'Zip') VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (name, email, geo_lat, geo_lon, altitude, geomagnetic_lat, zip))
        #cur.execute("INSERT INTO Subscribers(Email) VALUES ('%s');" % email)
        #cur.executemany("INSERT INTO Subscribers VALUES(?, ?)", insertStatement)
        con.commit

#def create_user(name, email, glat, glon, geomag, zip_code):
#    con = lite.connect('aurora_simple.db')
#    insertStatement = (
#                    (name, email, glat, glon, geomag, zip_code)
#                       )
#    with con:
#        cur = con.cursor()
#        cur.executemany("INSERT INTO Subscribers VALUES(?, ?, ?, ?, ?, ?)", insertStatement)
#    print "creating user derp"
    
#createSimpleDB()
    
#create_db()