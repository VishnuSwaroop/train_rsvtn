import MySQLdb
import getpass
from Tkinter import *

from ttk import *
import ttk
import tkMessageBox
import tkFont
from tkFont import *
import sqlcommands
from sqlcommands import *
import json
class school_info_page:
    def __init__(self, db1):
        with open('userinfo.json', 'r') as outfile:
            user_info=json.load(outfile)
            self.cust_username=user_info["Username"]
            print('The current user is %s'%(self.cust_username))
        
        self.db=db1
        self.cur = self.db.cursor()
 
        self.root1 = Toplevel()
        
        self.root1.title("GT Train Reservation System - Team 45")
        
        self.add_school= ttk.Frame(self.root1, padding="300 300 350 350")
        
        self.add_school.grid(column=0, row=0, sticky=(N, W, E, S))
        self.add_school.columnconfigure(0, weight=1)
        self.add_school.rowconfigure(0, weight=1)
        
        
        
        appHighlightFont= tkFont.Font(family="Helvetica",size=30,weight="bold")
        
        
        l1=ttk.Label(self.add_school, text="Add school info",font=appHighlightFont).grid(column=2, row=1, sticky=W)
        self.school_email = StringVar()
        
        self.school_email_entry = ttk.Entry(self.add_school, width=15, textvariable=self.school_email)
        self.school_email_entry.grid(column=3, row=3, sticky=(W, E))
        
        l2=ttk.Label(self.add_school, text="Add school email:",font=appHighlightFont).grid(column=2, row=3, sticky=W)
        l3=ttk.Label(self.add_school, text="Enter emails that ends with '.edu'").grid(column=2, row=4, sticky=W)
        
        
        Button(self.add_school, text="Back", command=self.go_back).grid(column=2, row=7, sticky=W)
        Button(self.add_school, text="Submit", command=self.submit_school).grid(column=5, row=7, sticky=W)
        
    def go_back(self):
        self.root1.destroy()
    
    def submit_school(self):
        try:
            value1=str(self.school_email.get())
            #value2=str(self.email.get())

            if (value1[-4:] == ".edu"):
                self.cur.execute(statement9%(self.cust_username))
                tkMessageBox.showinfo(message="Successful")
                self.db.commit()
                print('Committing is done in add info page')
                self.root1.destroy()
            else:
                tkMessageBox.showinfo("Please enter valid school email")
                return
                   
        except ValueError:
            tkMessageBox.showinfo("Please enter valid info")
            return
    