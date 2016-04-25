
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


class customer_menu_page(webapp2.RequestHandler):
    def get(self):
        self.response.write(ALL_PAGE_HEADER)
        self.response.write('<p><h1><font color="red">Login Successful ! Welcome Customer</font>  </h1></p>')

        self.response.write(MENU_PAGE)  
    
    # def __init__(self, db1):
    #     with open('userinfo.json', 'r') as outfile:
    #         user_info=json.load(outfile)
    #         self.cust_username=user_info["Username"]
    #         print('The current user is %s'%(self.cust_username))
    #         
    #     self.db=db1
    #     self.cur = self.db.cursor()
    # 
    #     self.root1 = Toplevel()
    #     
    #     self.root1.title("GT Train Reservation System - Team 45")
    #     
    #     self.cust_menu= ttk.Frame(self.root1, padding="300 300 350 350")
    #     
    #     self.cust_menu.grid(column=0, row=0, sticky=(N, W, E, S))
    #     self.cust_menu.columnconfigure(0, weight=1)
    #     self.cust_menu.rowconfigure(0, weight=1)
    #     
    #     
    #     
    #     appHighlightFont= tkFont.Font(family="Helvetica",size=30,weight="bold")
    #     
    #     
    #     l1=ttk.Label(self.cust_menu, text="Choose Functionality",font=appHighlightFont).grid(column=2, row=1, sticky=W)
    #     
    #     
    # 
    #     Button(self.cust_menu, text="View train schedule", command=self.view_train_schedule).grid(column=2, row=3, sticky=W)
    #     Button(self.cust_menu, text="Make a new reservation", command=self.make_reserve).grid(column=2, row=5, sticky=W)
    #     Button(self.cust_menu, text="Update a reservation", command=self.update_reserve).grid(column=2, row=7, sticky=W)
    #     Button(self.cust_menu, text="Cancel a reservation", command=self.cancel_reserve).grid(column=2, row=9, sticky=W)
    #     Button(self.cust_menu, text="Give Review", command=self.give_review).grid(column=2, row=11, sticky=W)
    #     Button(self.cust_menu, text="Add school information", command=self.add_school).grid(column=2, row=13, sticky=W)
    #     Button(self.cust_menu, text="Logout", command=self.logout).grid(column=4, row=15, sticky=W)
    #     
    # 
    #     
    #     
    #     
    #     for child in self.cust_menu.winfo_children(): child.grid_configure(padx=5, pady=5)
    #     
    #     
    #     #self.username_entry.focus()
    #     
    #     self.root1.mainloop()
    #     
    #     
    # def view_train_schedule(self):
    #     train_schedule.train_schedule1(self.db)
    # def make_reserve(self):
    #     print('')
    # def update_reserve(self):
    #     print('')
    # def cancel_reserve(self):
    #     print('')
    # def give_review(self):
    #     print('')
    # def add_school(self):
    #     school_info.school_info_page(self.db)
    # def logout(self):
    #     print('')