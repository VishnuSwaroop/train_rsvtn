
import urllib
import time

import random
import json

import MySQLdb
import getpass
import datetime
import sqlcommands
from sqlcommands import *

import json


import urllib
import time

import random
import json
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from google.appengine.api import search
from templates import *

import webapp2

class updatereserve(webapp2.RequestHandler):
    def get(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        
        self.cur.execute(statement37 %(self.user_cookie))
        rsvnsmade=self.cur.fetchall()
        
        self.response.write('<h2 align="center"><b><font color="blue">Update Reservation</font>  </b></h2>')
        self.response.write(' <form action="/updatereserve2" method="post">')
        # self.response.write('<input list="stations" name="station">')
        self.response.write('<select name="rsvnid">')
        for i in range(len(rsvnsmade)):
            self.response.write('<option value="%s">%s</option>'%(str(rsvnsmade[i][0]),str(rsvnsmade[i][0])))

        self.response.write('</select>')
        self.response.write('<input type="submit">')
        self.response.write('</form>')
        
class updatereserve2(webapp2.RequestHandler):
    def post(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        rsvnid=str(self.request.get('rsvnid'))
        
        print'The selected rsvn id is :::::::::::;'
        print rsvnid
        self.cur.execute(statement38 % (rsvnid))
        self.db.commit()
        train_list=self.cur.fetchall()  #trainno
        self.cur.execute(statement39 % (rsvnid))
        self.db.commit()
        duration=self.cur.fetchall()  #fetch the duration
        self.cur.execute(statement40 % (rsvnid))
        self.db.commit()
        place_details=self.cur.fetchall() #departs from, arrives at, class
        self.cur.execute(statement41 % (rsvnid))
        self.db.commit()
        prices=self.cur.fetchall() #price
        self.cur.execute(statement42 % (rsvnid))
        self.db.commit()
        bag_details=self.cur.fetchall() #fetch the bag and passenger name
        
        self.response.write('<form action="/updatereserve3" method="post">')
        self.response.write('<table style="width:60%" border="3">')
        self.response.write('<tr>')
        self.response.write('<th>Train</th>')
        self.response.write('<th>Duration</th>')
        self.response.write('<th>Departs From</th>')
        self.response.write('<th>Arrives at</th>')
        self.response.write('<th>Class</th>')
        self.response.write('<th>Price</th>')
        self.response.write('<th>No of bags</th>')
        self.response.write('<th>Passenger Name</th>')
        self.response.write('</tr>')
        
        self.response.write('<tr>')
        #self.response.write('<td>')
        
        # google_username = ndb.StringProperty(indexed=False)
        # google_train = ndb.StringProperty(indexed=False)
        # google_duration = ndb.StringProperty(indexed=False)
        # google_departs = ndb.StringProperty(indexed=False)
        # google_arrives = ndb.StringProperty(indexed=False)
        # google_class = ndb.StringProperty(indexed=False)
        # google_price = ndb.StringProperty(indexed=False)
        # google_bags = ndb.StringProperty(indexed=False)
        # google_psngrname = ndb.StringProperty(indexed=False)
        # google_date=ndb.StringProperty(indexed=False)
        self.response.write('<td><b><font color="blue">%s</font>  </b></td>' % str(train_list[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(duration[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][1]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][2]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(prices[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(bag_details[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(bag_details[0][1]))
        
        self.response.write('<td>')
        
        self.response.write('<td><button name="select" type="submit" value="%s">%s</button>'% (track1,str(item[2])))
        # self.response.write('<input type="radio" name="updatersvn" value="updatersvn"><br>')
        # 
        self.response.write('</td>')
        self.response.write('</tr>')
        self.response.write('<p></p>')
                       
                
        
        self.response.write('</table>')
        self.response.write('<input type="submit" value="update">')
        
        self.response.write('</form> ')
        