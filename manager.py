
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

class manager_menu(webapp2.RequestHandler):
    def get(self):
        
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))
        self.response.write('<p><h1><font color="red">Login Successful ! Welcome Manager</font>  </h1></p>')
        self.cur = self.db.cursor()
        self.response.write(MANAGER_MENU_PAGE)
        
        
class revenue(webapp2.RequestHandler):
    def get(self):
        self.response.write(ALL_PAGE_HEADER)
        self.response.write('<a href=/manager_menu> <h2>Back to choose functionality</h2></a>')
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        self.cur.execute(statement61)
        revenue_report=self.cur.fetchall()
        self.db.commit()
        self.response.write('<h2><b><font color="blue">Revenue Report</font></b><h2>')
        self.response.write('<table style="width:60%" border="3">')
        self.response.write('<tr>')
        # self.response.write('<th>Train No</th>')
        self.response.write('<th>Month</th>')
        self.response.write('<th>Revenue</th>')
        #self.response.write('<th>Comment</th>')

        self.response.write('</tr>')
        
        
        for i in range(len(revenue_report)):
            #self.response.write('<table style="width:100%">')
            if revenue_report[i][0] != None:
                self.response.write('<tr>')
                #self.response.write('<td>')
    
                self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(revenue_report[i][0])))
                self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(revenue_report[i][1])))
       
    
                
                self.response.write('</tr>')
                self.response.write('<p></p>')
        #self.response.write('<li> <a href=/manager_menu> <h3>Back to choose functionality</h3></a>')
        
        
        
        
class pop_route(webapp2.RequestHandler):
    def get(self):
        self.response.write(ALL_PAGE_HEADER)
        self.response.write('<a href=/manager_menu> <h2>Back to choose functionality</h2></a>')
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        self.cur.execute(statement62)
        #reviews=self.cur.fetchall()
        self.db.commit()
        self.cur.execute(statement63)
        #reviews=self.cur.fetchall()
        self.db.commit()
        self.cur.execute(statement64)
        #reviews=self.cur.fetchall()
        self.db.commit()
        
        self.cur.execute(statement65)
        month1=self.cur.fetchall()
        self.db.commit()
        self.cur.execute(statement66)
        month2=self.cur.fetchall()
        self.db.commit()
        self.cur.execute(statement67)
        month3=self.cur.fetchall()
        self.db.commit()
        
        
        
        self.response.write('<h2><b><font color="blue">Popular route report</font></b><h2>')
        self.response.write('<table style="width:60%" border="3">')
        self.response.write('<tr>')
        # self.response.write('<th>Train No</th>')
        self.response.write('<th>Month</th>')
        self.response.write('<th>Train number</th>')
        self.response.write('<th>No. of Reservations</th>')

        self.response.write('</tr>')
        
        
        for i in range(len(month1)):
            #self.response.write('<table style="width:100%">')
            self.response.write('<tr>')
            #self.response.write('<td>')

            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month1[i][0])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month1[i][1])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month1[i][2])))
   

            
            self.response.write('</tr>')
            self.response.write('<p></p>')
            
        
        
        #self.response.write('<h2><b><font color="blue">Popular route report</font></b><h2>')
        self.response.write('<table style="width:60%" border="3">')
        self.response.write('<tr>')
        # self.response.write('<th>Train No</th>')
        self.response.write('<th>Month</th>')
        self.response.write('<th>Train number</th>')
        self.response.write('<th>No. of Reservations</th>')

        self.response.write('</tr>')
        
        
        for i in range(len(month2)):
            #self.response.write('<table style="width:100%">')
            self.response.write('<tr>')
            #self.response.write('<td>')

            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month2[i][0])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month2[i][1])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month2[i][2])))
 
            self.response.write('</tr>')
            self.response.write('<p></p>')
            
            
        self.response.write('<table style="width:60%" border="3">')
        self.response.write('<tr>')
        # self.response.write('<th>Train No</th>')
        self.response.write('<th>Month</th>')
        self.response.write('<th>Train number</th>')
        self.response.write('<th>No. of Reservations</th>')

        self.response.write('</tr>')
        
        
        for i in range(len(month3)):
            #self.response.write('<table style="width:100%">')
            self.response.write('<tr>')
            #self.response.write('<td>')

            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month3[i][0])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month3[i][1])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(month3[i][2])))
   

            
            self.response.write('</tr>')
            self.response.write('<p></p>')
            
        
        