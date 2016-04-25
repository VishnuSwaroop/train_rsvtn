
import urllib
import time

import random
import json

import MySQLdb
import getpass

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


class registration_page(webapp2.RequestHandler):

    def get(self):
        

        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(REG_PAGE)   
    def post(self):
        
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.username1= self.request.get('username')
        self.email= self.request.get('email')
        self.password1 = self.request.get('password')
        self.conf_password1 = self.request.get('conf_password')


        value1=self.username1
        value2=self.email
        value3=self.password1
        value4=self.conf_password1
        
        temp=self.cur.execute(statement7%(value1)) #username
        
        result=self.cur.fetchall()
        print result
        temp1=self.cur.execute(statement8%(value2)) #email
        result1=self.cur.fetchall()
        print result1
        
        
        
        print('The values in reg page are:')
        print (value1,value2,value3,value4)
    
        if ((bool(value1) and bool(value2) and bool(value3) and bool(value4)) == False):
            self.response.write('<p><h1><font color="red">Please enter all fields</font>  </h1></p>')
            self.response.write('<a href=/register> <h3 align="left"> Back to registration page </h3> </a>')
            return
            
        
        
        for i in ('!','~','@','#','$','%','^','&','*','(',')','_','-','+','=',':',';','<','>'):
                if ((i in str(value1)) or (i in str(value3))):
                    self.response.write('<p><h1><font color="red">No special characters allowed</font>  </h1></p>')
                    self.response.write('<a href=/register> <h3 align="left"> Back to registration page </h3> </a>')
                    return
        
        
        if result:
            self.response.write('<p><h1><font color="red">Please choose a different username</font>  </h1></p>')
            self.response.write('<a href=/register> <h3 align="left"> Back to registration page </h3> </a>')
            return
        elif result1:
            self.response.write('<p><h1><font color="red">Please choose a different email</font>  </h1></p>')
            self.response.write('<a href=/register> <h3 align="left"> Back to registration page </h3> </a>')
            return
            
                
                
                
                
                
        if (value3==value4):
            
            self.cur.execute(statement4%(value1,value3))
            
            if (value2[-4:] == ".edu"):
                self.cur.execute(statement6%(value1,value2,int(1)))
            else:
                self.cur.execute(statement5%(value1,value2))
                    
            self.response.write('<p><h1><font color="red">Registration Successfull</font>  </h1></p>')
            self.db.commit()
            print('Committing is done in registration page')
 
            #return
        else:
            self.response.write('<p><h1><font color="red">Passwords do not match</font>  </h1></p>')
            self.response.write('<a href=/register> <h3 align="left"> Back to registration page </h3> </a>')

    
