
import urllib
import time

import random
import json

import MySQLdb
import getpass

import sqlcommands
from sqlcommands import *

import json
import update
from update import *

import urllib
import time
from review import *
import random
import json
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from google.appengine.api import search
from cancel import *
from templates import *
import webapp2
from reg_page import *
from menu import *
#HTML page templates
from train_schedule import *
from school_info import *
from make_reserve import *
from manager import *
class login_page(webapp2.RequestHandler): 
 
    def get(self):
        
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(HOME_PAGE)   
        
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        
    def post(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(HOME_PAGE)  
        #username1 = self.request.get('username')




        value1= self.request.get('username')

        value2= self.request.get('password')

        if ((bool(value1) and bool(value2)) == False):
            self.response.write('<p><h1><font color="red">Please enter all fields</font>  </h1></p>')
            return
        print('The values in main are:')
        print(value1,value2)
        
        temp=self.cur.execute(statement1%(value1,value2))
        result=self.cur.fetchall()
        if result:
            temp1=self.cur.execute(statement2%(value1))
            result1=self.cur.fetchall()
            temp2=self.cur.execute(statement3%(value1))
            result2=self.cur.fetchall()
            if result1:
                user_dict={"Username":value1}

                # self.response.write('<p><h1><font color="red">Login Successful ! Welcome Customer</font>  </h1></p>')
                # self.response.write('<a href=/menu> <h3 align="left"> Go to menu </h3> </a>')
                #randomkey=random.randrange(1,1000)
                self.response.headers.add_header('Set-Cookie', 'Username=%s' % str(value1))
                self.response.write('<meta http-equiv="refresh" content="0; url=/menu" />')
                
            elif result2:
                self.response.write('<meta http-equiv="refresh" content="0; url=/manager_menu" />')
                

            return
            
        else:
            self.response.write('<p><h1><font color="red">Login Failed </font>  </h1></p>')
    
    
    


app = webapp2.WSGIApplication([
    ('/',login_page ),
    ('/register',registration_page),
    ('/menu',customer_menu_page),
    ('/viewschedule',train_schedule1),
    ('/makereserve',make_reservation),
    ('/updatereserve',updatereserve),
    ('/updatereserve2',updatereserve2),
    ('/updatereserve3',updatereserve3),
    ('/updateconf',updateconf),
    ('/cancelreserve',cancelreserve),
    ('/cancelreserve2',cancelreserve2),
    
    ('/cancelconf',cancelconf),
    #('/givereview',give_review),
    ('/viewreview',view_review),
    ('/viewreview2',view_review2),
    ('/givereview',give_review),
    ('/givereview2',give_review2),
    ('/addschool',school_info_page),
    ('/selectdep',sel_dep_page),
    ('/pngr_info',pngr_info),
    ('/finalreserve',finalreserve),
    ('/paymentinfo',paymentinfo),
    ('/confirmation',confirmation),
    ('/manager_menu', manager_menu),
    ('/revenue', revenue),
    ('/pop_route', pop_route)

    
], debug=True)