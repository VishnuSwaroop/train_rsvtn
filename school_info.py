
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


class school_info_page(webapp2.RequestHandler):
    def get(self):
        # self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
        #              user="root",         # your username
        #              passwd="r0cknr0lla",  # your password
        #              db="trainsystem")        # name of the data base
        # 
        # self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(SCHOOL_PAGE)
        # value1=self.request.get('schoolemail')
        
    def post(self):
        self.user_cookie=self.request.cookies.get('Username')
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(SCHOOL_PAGE)
        value1=self.request.get('schoolemail')
            #value2=str(self.email.get())
    
        if (value1[-4:] == ".edu"):
            self.cur.execute(statement9%(self.user_cookie))
            self.response.write('<p><h1><font color="red">School info added</font>  </h1></p>')
            self.db.commit()
            print('Committing is done in add info page')
        else:
            self.response.write('<p><h1><font color="red">Please enter valid school id</font>  </h1></p>')
            return
    
    
    
    
    
    #     self.root1 = Toplevel()
    #     
    #     self.root1.title("GT Train Reservation System - Team 45")
    #     
    #     self.add_school= ttk.Frame(self.root1, padding="300 300 350 350")
    #     
    #     self.add_school.grid(column=0, row=0, sticky=(N, W, E, S))
    #     self.add_school.columnconfigure(0, weight=1)
    #     self.add_school.rowconfigure(0, weight=1)
    #     
    #     
    #     
    #     appHighlightFont= tkFont.Font(family="Helvetica",size=30,weight="bold")
    #     
    #     
    #     l1=ttk.Label(self.add_school, text="Add school info",font=appHighlightFont).grid(column=2, row=1, sticky=W)
    #     self.school_email = StringVar()
    #     
    #     self.school_email_entry = ttk.Entry(self.add_school, width=15, textvariable=self.school_email)
    #     self.school_email_entry.grid(column=3, row=3, sticky=(W, E))
    #     
    #     l2=ttk.Label(self.add_school, text="Add school email:",font=appHighlightFont).grid(column=2, row=3, sticky=W)
    #     l3=ttk.Label(self.add_school, text="Enter emails that ends with '.edu'").grid(column=2, row=4, sticky=W)
    #     
    #     
    #     Button(self.add_school, text="Back", command=self.go_back).grid(column=2, row=7, sticky=W)
    #     Button(self.add_school, text="Submit", command=self.submit_school).grid(column=5, row=7, sticky=W)
    #     
    # def go_back(self):
    #     self.root1.destroy()
    # 
    # def submit_school(self):
    #     try:
    #         value1=str(self.school_email.get())
    #         #value2=str(self.email.get())
    # 
    #         if (value1[-4:] == ".edu"):
    #             self.cur.execute(statement9%(self.cust_username))
    #             tkMessageBox.showinfo(message="Successful")
    #             self.db.commit()
    #             print('Committing is done in add info page')
    #             self.root1.destroy()
    #         else:
    #             tkMessageBox.showinfo("Please enter valid school email")
    #             return
    #                
    #     except ValueError:
    #         tkMessageBox.showinfo("Please enter valid info")
    #         return
    # 