import sqlite3 as lite
import sys


#
# Not creating the schema properly.
#
def create_db():
    con = lite.connect('aurora_db.db')
    with con:
        cur = con.cursor()    
        cur.execute("CREATE TABLE Subscribers(Id INTEGER PRIMARY KEY, Name TEXT, Email TEXT, Geographic_Lat INT, Geographic_Lon INT, Altitude_km INT, Geomagnetic_Lat INT, Geomagnetic_Lon INT, Threshold INT, Pin INT);")
        
def create_user(name, email, glat, glon, zip_code):
    con = lite.connect('aurora_db.db')
    insertStatement = (
                    (name, email, glat, glon, 0, 0, 0, 0, 0, zip_code)
                       )
    with con:
        cur = con.cursor()
        cur.executemany("INSERT INTO Subscribers VALUES(?, ?, ?, ?)", insertStatement)
    print "creating user derp"
    
#create_db()