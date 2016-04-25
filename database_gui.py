#!/usr/bin/python
import MySQLdb
import getpass
from Tkinter import *

from ttk import *
import ttk
import tkMessageBox
import tkFont
from tkFont import *
from reg_page import *
import reg_page
import sqlcommands
from sqlcommands import *

import json

from menu import *
import menu
# 
# def main():
#     login_page()


class login_page:

    def __init__(self):
    
        self.password1=getpass.getpass()
        # db = MySQLdb.connect(host="academic-mysql.cc.gatech.edu",    # your host, usually localhost
        #                      user="vswaroop3",         # your username
        #                      passwd=password1,  # your password
        #                      db="cs4400_Team_45")        # name of the data base
        
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd=self.password1,  # your password
                             db="trainsystem")        # name of the data base
        
        
        
        
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        
        

        self.cur = self.db.cursor()
 
        self.root = Tk()
        
        self.root.title("GT Train Reservation System - Team 45")
        
        self.login= ttk.Frame(self.root, padding="300 300 350 350")
        
        self.login.grid(column=0, row=0, sticky=(N, W, E, S))
        self.login.columnconfigure(0, weight=1)
        self.login.rowconfigure(0, weight=1)
        
        self.username= StringVar()
        self.password = StringVar()
        
        self.username_entry = ttk.Entry(self.login, width=15, textvariable=self.username)
        self.username_entry.grid(column=3, row=3, sticky=(W, E))
        
        self.password_entry = ttk.Entry(self.login, width=15, textvariable=self.password)
        self.password_entry.grid(column=3, row=5, sticky=(W, E))
        
        
        
        appHighlightFont= tkFont.Font(family="Helvetica",size=30,weight="bold")
        
        
        l1=ttk.Label(self.login, text="Login",font=appHighlightFont).grid(column=2, row=1, sticky=W)
        l2=ttk.Label(self.login, text="Username :",font=appHighlightFont).grid(column=2, row=3, sticky=W)
        l3=ttk.Label(self.login, text="Password :",font=appHighlightFont).grid(column=2, row=5, sticky=W)
        
               
        
        
        Button(self.login, text="Login", command=self.checkuser).grid(column=2, row=7, sticky=W)
        Button(self.login, text="Register", command=self.openreg).grid(column=3, row=7, sticky=E)
        
        
        
        for child in self.login.winfo_children(): child.grid_configure(padx=5, pady=5)
        
        
        self.username_entry.focus()
        
        self.root.mainloop()
    
        self.db.commit()
        print 'Committing is done in main'
        self.db.close()
    
    def checkuser(self):
            try:
                value1 = str(self.username.get())
                value2= str(self.password.get())
                if ((bool(value1) and bool(value2)) == False):
                    tkMessageBox.showinfo(message="Please enter all fields")
                    return
                print('The values in main are:')
                print(value1,value2)
                
                temp=self.cur.execute(statement1%(value1,value2))
                result=self.cur.fetchall()
                if result:
                    #tkMessageBox.showinfo(message="Login Successful !")
                    temp1=self.cur.execute(statement2%(value1))
                    result1=self.cur.fetchall()
                    temp2=self.cur.execute(statement3%(value1))
                    result2=self.cur.fetchall()
                    if result1:
                        user_dict={"Username":value1}
                        with open('userinfo.json', 'w') as outfile:
                            json.dump(user_dict,outfile, indent=4,sort_keys=True)
                            print('User info written to file')
                        tkMessageBox.showinfo(message="Login Successful ! Welcome Customer")
                        
                        # user_dict={"Username":value1}
                        # with open('userinfo.json', 'w') as outfile:
                        #     json.dump(user_dict, indent=4,sort_keys=True)
                        #     print('User info written to file')
                        
                        self.openmenu()
                        
                    elif result2:
                        tkMessageBox.showinfo(message="Login Successful ! Welcome Manager")

                    return
                    
                else:
                    tkMessageBox.showinfo(message="Login Failed !")
                    return
            except ValueError:
                tkMessageBox.showinfo("Please enter valid info")
                return
    
    def openreg(self):
        registration_page(self.db)
        
    def openmenu(self):
        
        customer_menu_page(self.db)
        
if __name__ == "__main__":
    login_page()