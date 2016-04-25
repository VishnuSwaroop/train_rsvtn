
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

class cancelreserve(webapp2.RequestHandler):
    def get(self):
         
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        
        self.cur.execute(statement50 %(self.user_cookie))
        rsvnsmade=self.cur.fetchall()
        
        self.response.write('<h2 align="center"><b><font color="blue">Cancel Reservation</font>  </b></h2>')
        self.response.write(' <form action="/cancelreserve2" method="post">')
        # self.response.write('<input list="stations" name="station">')
        self.response.write('<select name="rsvnid">')
        for i in range(len(rsvnsmade)):
            self.response.write('<option value="%s">%s</option>'%(str(rsvnsmade[i][0]),str(rsvnsmade[i][0])))

        self.response.write('</select>')
        self.response.write('<input type="submit">')
        self.response.write('</form>')
        
class cancelreserve2(webapp2.RequestHandler):
    def post(self):
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        rsvnid=str(self.request.get('rsvnid'))
        rsvn_cookie=str(self.request.cookies.get('resIDtrainNO1'))
        trainno_cookie=str(self.request.cookies.get('resIDtrainNO2'))
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
        
        self.response.write('<form action="/cancelconf" method="post">')
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
        # track1=unicode(rsvnid)+","+unicode(train_list[0][0])
        track1=unicode(rsvn_cookie)
        self.response.write('<td><button name="select" type="submit" value="%s">Cancel</button>'% (track1))
        # self.response.write('<input type="radio" name="updatersvn" value="updatersvn"><br>')
        # 
        self.response.write('</td>')
        self.response.write('</tr>')
        self.response.write('<p></p>')
                       
                
        
        self.response.write('</table>')
        
        self.totalcost=str(self.request.cookies.get('totalcost'))
        
        print str(rsvnid)
        
        self.cur.execute(statement55 %(str(rsvnid)))
        self.db.commit()
        difference=self.cur.fetchall()
        refund_amt=0
        
        print ('DIFFERENCE IS :::::::::::::')
        print difference
        print self.totalcost
        
        if (int(difference[0][0]) >= 7):
            refund_amt=(int(self.totalcost)*0.8)-50
        elif (int(difference[0][0])<7 and int(difference[0][0])>1):
            refund_amt=(int(self.totalcost)*0.5)-50
        elif(int(difference[0][0]) <1):
            self.response.write('<h3><p>The reservation date has already passed !</p></h3>')
        elif refund_amt<0:
            refund_amt=0
        else:
            refund_amt=0
        
        self.response.write('<h2><b>Amount to be refunded : %s</b></h2>' %(str(refund_amt)))
        
        #self.response.write('<input type="submit" value="update">')
        
        self.response.write('</form> ')
        

class cancelconf(webapp2.RequestHandler):
    def post(self):
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))
        
        rsvn=str(self.request.cookies.get('resIDtrainNO1'))
        trainno=str(self.request.cookies.get('resIDtrainNO2'))
        self.cur = self.db.cursor()
        #update_date=str(self.request.get('update_date'))
        #rsvnid=str(self.request.get('select'))
        
        print (rsvn,trainno)
        # print ('DEP DATE IS ::::::::')
        # print update_date
        self.cur.execute(statement56 % (str(rsvn)))
        self.db.commit()

        
        self.response.write('<h2><b>Reservation has been cancelled !</b></h2>')
        
        