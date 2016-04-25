
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
         
        self.response.write(ALL_PAGE_HEADER)
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
        self.response.write(ALL_PAGE_HEADER)
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
        track1=unicode(rsvnid)+","+unicode(train_list[0][0])
        self.response.write('<td><button name="select" type="submit" value="%s">select</button>'% (track1))
        # self.response.write('<input type="radio" name="updatersvn" value="updatersvn"><br>')
        # 
        self.response.write('</td>')
        self.response.write('</tr>')
        self.response.write('<p></p>')
                       
                
        
        self.response.write('</table>')
        self.response.write('<input type="submit" value="update">')
        
        self.response.write('</form> ')
        
class updatereserve3(webapp2.RequestHandler):
    def post(self):
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        rsvnid=str(self.request.get('select'))
        rsvnids=rsvnid.split(',')
        print'The selected rsvn information is :::::::::::;'
        print rsvnids
        self.cur.execute(statement43 % (str(rsvnids[0]),str(rsvnids[1])))
        self.db.commit()
        duration=self.cur.fetchall()  #trainno
        self.cur.execute(statement44 % (str(rsvnids[0]),str(rsvnids[1])))
        self.db.commit()
        place_details=self.cur.fetchall()  #fetch the duration
        self.cur.execute(statement45 % (str(rsvnids[0]),str(rsvnids[1])))
        self.db.commit()
        prices=self.cur.fetchall() #departs from, arrives at, class
        self.cur.execute(statement46 % (str(rsvnids[0]),str(rsvnids[1])))
        self.db.commit()
        bag_details=self.cur.fetchall() #price
        
        i = datetime.datetime.now()
        today_date=str(str(i.year)+"-"+"0"+str(i.month)+"-"+str(i.day))
        
        
        self.cur.execute(statement47 % (str(rsvnids[0]),str(rsvnids[1])))
        self.db.commit()
        dep_dates=self.cur.fetchall() #fetch the bag and passenger name
        dep_date=str(dep_dates[0][0])
        self.response.write('<form action="/updateconf" method="post">')
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
        self.response.write('<td><b><font color="blue">%s</font>  </b></td>' % str(rsvnids[1]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(duration[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][1]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][2]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(prices[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(bag_details[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(bag_details[0][1]))
        
        self.response.write('<td>')
        #track1=unicode(rsvnids[0])+","+unicode(rsvnids[1])
        track1=str(rsvnids[0])+","+str(rsvnids[1])
        
        
        self.response.write('<input name="update_date" type="date" min="%s" max="%s"/>'%(today_date,dep_date))
        
        #self.response.write('<td><button name="select" type="submit" value="%s">Update</button>'% (track1))
        # self.response.write('<input type="radio" name="updatersvn" value="updatersvn"><br>')
        # 
        self.response.write('</td>')
        self.response.write('</tr>')
        self.response.write('<p></p>')
                       
                
        
        self.response.write('</table>')
        self.response.write('<input type="submit" value="Update">')
        
        self.response.write('</form> ')
        
        self.cur.execute(statement49)
        self.db.commit()
        change_fee=self.cur.fetchall() #fetch the bag and passenger name
        
        fee=change_fee[0][0]
        self.cur.execute(statement23)
        self.db.commit()
        studentstatus=self.cur.fetchall() #fetch the whether student or not
        
        
        print ('student status is :::::::::::')
        print studentstatus[0][0]
        totalcost=0
        self.response.write('</table>')
        if studentstatus[0][0]==True:    
            self.response.write('<p><h3><b>Student discount applied</b><h3></p>')
            if int(bag_details[0][0])==3:
                totalcost=((int(prices[0][0])+30)*0.8)
                totalcost=totalcost+int(fee)
            elif int(bag_details[0][0])==4:
                totalcost=((int(prices[0][0])+60)*0.8)
                totalcost=totalcost+int(fee)
            else:
                totalcost=((int(prices[0][0])*0.8))
                totalcost=totalcost+int(fee)
        elif studentstatus[0][0]==False:    
            self.response.write('<p><h3><b>Student discount NOT applied</b><h3></p>')
            if int(bag_details[0][0])==3:
                totalcost=((int(prices[0][0])+30))
                totalcost=totalcost+int(fee)
            elif int(bag_details[0][0])==4:
                totalcost=((int(prices[0][0])+60))
                totalcost=totalcost+int(fee)
            else:
                totalcost=((int(prices[0][0])))
                totalcost=totalcost+int(fee)
        
        self.response.write('<h3><b>Total Cost : %s</b><h3>'%(totalcost))
        
        
        
        print ('TRACK 1 IS ::::::::::;')
        print track1
        self.response.headers.add_header('Set-Cookie', 'resIDtrainNO1=%s' % (str(rsvnids[0])))
        self.response.headers.add_header('Set-Cookie', 'resIDtrainNO2=%s' % (str(rsvnids[1])))
        self.response.headers.add_header('Set-Cookie', 'totalcost=%s' % (str(totalcost)))
                                         
class updateconf(webapp2.RequestHandler):
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
        update_date=str(self.request.get('update_date'))
        #rsvnid=str(self.request.get('select'))
        
        print (rsvn,trainno)
        print ('DEP DATE IS ::::::::')
        print update_date
        self.cur.execute(statement48 % (update_date,str(rsvn),str(trainno)))
        self.db.commit()
        
        self.response.write('<h2><b>Reservation has been updated !</b></h2>')
        
        