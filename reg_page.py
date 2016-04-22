#!/usr/bin/python
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
# 
# def main():
#     register_page()


class registration_page():

    def __init__(self,db1):
    
        #password11=getpass.getpass()
        # db = MySQLdb.connect(host="academic-mysql.cc.gatech.edu",    # your host, usually localhost
        #                      user="vswaroop3",         # your username11
        #                      passwd=password11,  # your password1
        #                      db="cs4400_Team_45")        # name of the data base
        
        # self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
        #                      user="root1",         # your username1
        #                      passwd=password11,  # your password1
        #                      db="cs4400_Team_45")        # name of the data base
        
        
        
        
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        

        self.db=db1
        self.cur = self.db.cursor()
 
        self.root1 = Toplevel()
        
        self.root1.title("GT Train Reservation System - Team 45")
        
        self.register= ttk.Frame(self.root1, padding="300 300 350 350")
        
        self.register.grid(column=0, row=0, sticky=(N, W, E, S))
        self.register.columnconfigure(0, weight=1)
        self.register.rowconfigure(0, weight=1)
        
        self.username1= StringVar()
        self.email= StringVar()
        self.password1 = StringVar()
        self.conf_password1 = StringVar()
        
        self.username1_entry = ttk.Entry(self.register, width=15, textvariable=self.username1)
        self.username1_entry.grid(column=3, row=3, sticky=(W, E))
        
        self.password1_entry = ttk.Entry(self.register, width=15, textvariable=self.password1)
        self.password1_entry.grid(column=3, row=7, sticky=(W, E))
        
        self.email_entry = ttk.Entry(self.register, width=15, textvariable=self.email)
        self.email_entry.grid(column=3, row=5, sticky=(W, E))
        
        self.conf_password1_entry = ttk.Entry(self.register, width=15, textvariable=self.conf_password1)
        self.conf_password1_entry.grid(column=3, row=9, sticky=(W, E))
        
        
        
        appHighlightFont= tkFont.Font(family="Helvetica",size=30,weight="bold")
        
        
        l1=ttk.Label(self.register, text="Registration",font=appHighlightFont).grid(column=2, row=1, sticky=W)
        l2=ttk.Label(self.register, text="Username :",font=appHighlightFont).grid(column=2, row=3, sticky=W)
        l2=ttk.Label(self.register, text="Email :",font=appHighlightFont).grid(column=2, row=5, sticky=W)
        l2=ttk.Label(self.register, text="Password :",font=appHighlightFont).grid(column=2, row=7, sticky=W)
        l3=ttk.Label(self.register, text="Confirm Password :",font=appHighlightFont).grid(column=2, row=9, sticky=W)
        
               
        
        
        # Button(self.register, text="Login", command=self.checkuser).grid(column=2, row=7, sticky=W)
        Button(self.register, text="Register", command=self.storeuser).grid(column=3, row=11, sticky=W)
        
        
        
        for child in self.register.winfo_children(): child.grid_configure(padx=5, pady=5)
        
        
        self.username1_entry.focus()
        
        self.root1.mainloop()
        
    
    def storeuser(self):
            try:
                value1=str(self.username1.get())
                value2=str(self.email.get())
                value3=str(self.password1.get())
                value4=str(self.conf_password1.get())
                temp=self.cur.execute(statement7%(value1)) #username
                
                result=self.cur.fetchall()
                print result
                temp1=self.cur.execute(statement8%(value2)) #email
                result1=self.cur.fetchall()
                print result1
                
                
                
                print('The values in reg page are:')
                print (value1,value2,value3,value4)
            
                if ((bool(value1) and bool(value2) and bool(value3) and bool(value4)) == False):
                    tkMessageBox.showinfo(message="Please enter all fields")
                    return
                
                
                for i in ('!','~','@','#','$','%','^','&','*','(',')','_','-','+','=',':',';','<','>'):
                        if ((i in str(value1)) or (i in str(value3))):
                            tkMessageBox.showinfo(message="No special characters allowed")
                            return
                            
                
                
                
                if result:
                    tkMessageBox.showinfo(message="Please choose a different Username")
                    return
                    
                elif result1:
                    tkMessageBox.showinfo(message="Please choose a different email")
                    return
            
                
                
                
                
                
                if (value3==value4):
                    
                    self.cur.execute(statement4%(value1,value3))
                    
                    if (value2[-4:] == ".edu"):
                        self.cur.execute(statement6%(value1,value2,int(1)))
                    else:
                        self.cur.execute(statement5%(value1,value2))
                            
                    tkMessageBox.showinfo(message="Registration Successful")
                    self.db.commit()
                    print('Committing is done in registration page')
                    self.root1.destroy()
                    #return
                else:
                    tkMessageBox.showinfo(message="Passwords do not match")
                    return
            except ValueError:
                tkMessageBox.showinfo("Please enter valid info")
                return
    
