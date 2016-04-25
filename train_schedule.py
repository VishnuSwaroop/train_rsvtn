
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


class train_schedule1(webapp2.RequestHandler):
    def get(self):
        # self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
        #                      user="root",         # your username
        #                      passwd="r0cknr0lla",  # your password
        #                      db="trainsystem")        # name of the data base
        # 
        # self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(SCHEDULE_PAGE)
    def post(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(SCHEDULE_PAGE)
        value1=self.request.get('trainno')
        #value2=str(self.email.get())
        
        t1=self.cur.execute(statement10%(value1))
        result=self.cur.fetchall()
        # t2=self.cur.execute(statement11%(value1))
        # result1=self.cur.fetchall()
        t1=list(result)
        if t1:
            self.response.write('<b><font color="blue">Schedule for Train No %s</font>  </b>' % (str(value1)))
            self.response.write('<table style="width:60%" border="3">')
            self.response.write('<tr>')
            # self.response.write('<th>Train No</th>')
            self.response.write('<th>Arrival Time</th>')
            self.response.write('<th>Departure Time</th>')
            self.response.write('<th>Station Name</th>')
            self.response.write('<th>Location</th>')
            self.response.write('</tr>')
            
            
            for route in t1:
                #self.response.write('<table style="width:100%">')
                self.response.write('<tr>')
                #self.response.write('<td>')

                self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(route[1])))
                self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(route[2])))
                self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(route[3])))
                self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(route[4])))
                
                self.response.write('</tr>')
                self.response.write('<p></p>')
                
        
            
            self.response.write('</table>')
        else:
            self.response.write('<b><font color="blue">Train not found</font></b>')
            return
        
 
    #     self.root1 = Toplevel()
    #     
    #     self.root1.title("GT Train Reservation System - Team 45")
    #     
    #     self.train_sched= ttk.Frame(self.root1, padding="400 400 550 550")
    #     
    #     self.train_sched.grid(column=0, row=0, sticky=(N, W, E, S))
    #     self.train_sched.columnconfigure(0, weight=1)
    #     self.train_sched.rowconfigure(0, weight=1)
    #     
    #     
    #     
    #     appHighlightFont= tkFont.Font(family="Helvetica",size=30,weight="bold")
    #     
    #     
    #     l1=ttk.Label(self.train_sched, text="View Train Schedule",font=appHighlightFont).grid(column=2, row=1, sticky=W)
    #     self.train_no = StringVar()
    #     
    #     self.train_no_entry = ttk.Entry(self.train_sched, width=15, textvariable=self.train_no)
    #     self.train_no_entry.grid(column=3, row=3, sticky=(W, E))
    #     
    #     l2=ttk.Label(self.train_sched, text="Train No :",font=appHighlightFont).grid(column=2, row=3, sticky=W)
    #     #l3=ttk.Label(self.train_sched, text="Enter emails that ends with '.edu'").grid(column=2, row=4, sticky=W)
    #     
    #     
    #     Button(self.train_sched, text="Back", command=self.go_back).grid(column=2, row=7, sticky=W)
    #     Button(self.train_sched, text="Search", command=self.train_search).grid(column=5, row=7, sticky=W)
    #     
    # def go_back(self):
    #     self.root1.destroy()
    # 
    # def train_search(self):
    #     appHighlightFont= tkFont.Font(family="Helvetica",size=20,weight="bold")
    #     try:
    #         value1=str(self.train_no.get())
    #         #value2=str(self.email.get())
    #         
    #         t1=self.cur.execute(statement10%(value1))
    #         result=self.cur.fetchall()
    #         t2=self.cur.execute(statement11%(value1))
    #         result1=self.cur.fetchall()
    #         t1=list(result)
    #         list1=["Train No","Arrival Time","Depart Time","Name","Location"]
    #         # for i in range(5):
    #         #     l12=ttk.Label(self.train_sched, text=(list1[i]),font=appHighlightFont).grid(column=(1+i), row=11, sticky=(W))
    #         
    #         for i in range(3):
    #             for j in range(5):
    #                 l1=ttk.Label(self.train_sched, text=("%s"%(str(t1[i][j]))),font=appHighlightFont).grid(column=(int(j)), row=(12+int(i)), sticky=(W))
    #                 #l2=ttk.Label(self.train_sched, text="Train No :",font=appHighlightFont).grid(column=2, row=3, sticky=W)
    #         
    #                
    #     except ValueError:
    #         tkMessageBox.showinfo("Please enter valid info")
    #         return
    #     
    #     
    #     
    # def create_widgets(self):
    #     self.entries = {}
    #     self.tableheight = 9
    #     self.tablewidth = 9
    #     counter = 0
    #     for row in xrange(self.tableheight):
    #         for column in xrange(self.tablewidth):
    #             self.entries[counter] = Entry(self, width=5)
    #             self.entries[counter].grid(row=row, column=column)
    #             counter += 1
    # 