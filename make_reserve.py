
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

# 
# 
# def repository_key(mykey):
#     """Constructs a Datastore key for a repository entity.
# 
#     We use genre as the key.
#     """
#     return ndb.Key('Repository', mykey)
# 
# 
# 
# class g_reservation(ndb.Model):
#     """A main model for representing an individual reserve entry."""
#     google_username = ndb.StringProperty(indexed=False)
#     google_train = ndb.StringProperty(indexed=False)
#     google_duration = ndb.StringProperty(indexed=False)
#     google_departs = ndb.StringProperty(indexed=False)
#     google_arrives = ndb.StringProperty(indexed=False)
#     google_class = ndb.StringProperty(indexed=False)
#     google_price = ndb.StringProperty(indexed=False)
#     google_bags = ndb.StringProperty(indexed=False)
#     google_psngrname = ndb.StringProperty(indexed=False)
#     google_date=ndb.StringProperty(indexed=False)





class make_reservation(webapp2.RequestHandler):
    def get(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))
        print('THE USER IS ::::::::::::::::::::')
        print (str(self.user_cookie))
        self.cur = self.db.cursor()
        
        self.cur.execute(statement14)
        self.db.commit()
        #self.cur.execute(statement9%(self.user_cookie))
        self.cur.execute(statement25%(self.user_cookie))
        self.db.commit()
        self.cur.execute(statement26%(str(self.user_cookie)))
        self.db.commit()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write(SEARCH_TRAIN_PAGE)
        
        
        t1=self.cur.execute(statement11)
        self.db.commit()
        station_names=self.cur.fetchall()
        self.response.write('<b><font color="blue">Departs From : </font>  </b>')
        self.response.write(' <form action="/makereserve" method="post">')
        # self.response.write('<input list="stations" name="station">')
        self.response.write('<select name="station">')
        for i in range(len(station_names)):
            self.response.write('<option value="%s">%s</option>'%(str(station_names[i][0]),str(station_names[i][0])))

        self.response.write('</select>')
        self.response.write('<input type="submit">')
        self.response.write('</form>')
        self.db.commit()
    def post(self):
        self.user_cookie=self.request.cookies.get('Username')
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        

        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write('<h2 align="center">Seach Train</h2>')
        chosen_stn=str(self.request.get('station'))
        self.response.write('<h2 align="center">Chosen Departure Station : %s</h2>'%(chosen_stn))
        
        self.cur.execute(statement15%(chosen_stn)) # ADDING ONLY DEPARTURE STATION TO DATABASE#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<15
        self.db.commit()
        
        # t1=self.cur.execute(statement11)
        # station_names=self.cur.fetchall()
        # self.response.write('<b><font color="blue">Departs From : </font>  </b>')
        # self.response.write(' <form action="/makereserve" method="post">')
        # #self.response.write('<input list="stations" name="station">')
        # self.response.write('<select name="station">')
        # for i in range(len(station_names)):
        #     print str(station_names[i][0])
        #     print chosen_stn
        #     if (str(station_names[i][0]) == chosen_stn):
        #         self.response.write('<option value="%s" selected>%s</option>'%(str(station_names[i][0]),str(station_names[i][0])))
        #     else:
        #         self.response.write('<option value="%s">%s</option>'%(str(station_names[i][0]),str(station_names[i][0])))
        #     
        # self.response.write('</select>')
        # self.response.write('<input type="submit">')
        # self.response.write('</form>')
        
        i = datetime.datetime.now()
        today_date=str(str(i.year)+"-"+"0"+str(i.month)+"-"+str(i.day))
        print ('DATE IS :::::::::::::: %s'%today_date)
        
        t2=self.cur.execute(statement12%(chosen_stn)) #Getting destination options for selected train
        self.db.commit()
        dst_names=self.cur.fetchall()
        self.response.write('<b><font color="blue">Arrives at : </font>  </b>')
        self.response.write(' <form action="/selectdep" method="post">')
        self.response.write('<select name="destinations">')
        for i in range(len(dst_names)):
            self.response.write('<option value="%s">%s</option>'%(str(chosen_stn)+","+str(dst_names[i][0]),str(dst_names[i][0])))

        self.response.write('</select>')
        # self.response.write(' <form action="/makereserve" method="post">')
        self.response.write('<input name="booking_date" type="date" min="%s"/>'%(today_date))
        
        self.response.write('<input type="submit">Find trains')
        
        self.response.write('</form>')
        # 
        # destination=str(self.request.get('destinations'))
        # book_date=str(self.request.get('booking_date'))
        # 
        # if (bool(destination) and bool(book_date)):
        # 
        #     destination1=(destination.split(','))[1]
        #     chosen_stn1=(destination.split(','))[0]
        #     temp_dict={"Username":self.user_cookie, "Source":chosen_stn1,"Destination": destination1, "Date":book_date}
        #     #res_cooki=json.dumps(str(self.user_cookie)+","+str(chosen_stn1)+","+str(destination1)+","+str(book_date))
        #     print('temp dict is :')
        #     print(temp_dict)
        #     # self.response.headers.add_header('Set-Cookie', 'Reservation=%s' % (res_cooki))
        #     self.response.write('<meta http-equiv="refresh" content="0; url=/selectdep" />')
        #     # with open('reservation.json','w') as outputfile:
        #     #     json.dump(temp_dict,outputfile,indent=4,sort_keys=True)
        
        self.db.commit()
class sel_dep_page(webapp2.RequestHandler):
    # def get(self):
    #     #self.user_cookie=self.request.cookies.get('Reservation')
    #     #reservation_list=self.user_cookie.split(',')
    #     #print reservation_list
    #     #self.user_cookie=self.request.cookies.get('Username')
    #     self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    #                  user="root",         # your username
    #                  passwd="r0cknr0lla",  # your password
    #                  db="trainsystem")        # name of the data base
    #     
    #     self.cur = self.db.cursor()
    #     self.response.write(ALL_PAGE_HEADER)
    #     
    #     
    #     value1=str(reservation_list[1])
    #     print('Search String: %s' %(value1))
    #     t1=self.cur.execute(statement13%(value1))
    #     result=self.cur.fetchall()
    #     
    #     result=list(result)
    #     #self.response.write(SEARCH_TRAIN_PAGE)
    #     self.response.write('<h2 align="center"><b><font color="blue">Select Departure Page</font>  </b></h2>')
    #     self.response.write('<form action="/pngr_info" method="post">')
    #     self.response.write('<table style="width:60%" border="3">')
    #     self.response.write('<tr>')
    #     self.response.write('<th>Train</th>')
    #     self.response.write('<th>Duration</th>')
    #     self.response.write('<th>First Class Price</th>')
    #     self.response.write('<th>Second Class Price</th>')
    #     self.response.write('</tr>')
    #     for item in result:
    #         self.response.write('<tr>')
    #         #self.response.write('<td>')
    #         self.response.write('<td><b><font color="blue">%s</font> </b></td>' % str(item[0]))
    #         self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(item[1]))
    #         # self.response.write('<td><b><font color="green">$%s</font></b></td>' % str(item[2]))
    #         # self.response.write('<td>')
    #         track1=unicode(item[0])+","+unicode(item[1])+","+"first"+","+unicode(item[2])
    #         #track1=json.dumps(track1)
    #         # track1=unicode(track1)
    #         print track1
    #         track2=unicode(item[0])+","+unicode(item[1])+","+"second"+","+unicode(item[3])
    #         #track2=json.dumps(track2)
    #         # track2=unicode(track2)
    #         print track2
    #         
    #         self.response.write('<td><input type="radio" name="first" value="%s">%s<br>'% (track1,str(item[2])))#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #         self.response.write('<td><input type="radio" name="second" value="%s">%s<br>'% (track2,str(item[3])))
    #         self.response.write('</td>')
    #         self.response.write('</tr>')
    #         self.response.write('<p></p>')
    #                    
    #             
    #     
    #     self.response.write('</table>')
    #     self.response.write('<input type="submit" value="Next">')
    #     # self.response.write('<div ><h2><b><font color="green">Current Total: $%s <font></b></h2></div>' %(total_cost))
    #     self.response.write('</form> ')
    #     
    #     self.user_cookie=self.request.cookies.get('Reservation')
    #     reservation_list=self.user_cookie.split(',')
    #     print 'sel dep page::::::::::'
    #     print reservation_list
    #     
    
    def post(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.user_cookie=str(self.request.cookies.get('Username'))
        destination=str(self.request.get('destinations'))
        book_date=str(self.request.get('booking_date'))
        
        if (bool(destination) and bool(book_date)):

            destination1=(destination.split(','))[1]
            chosen_stn1=(destination.split(','))[0]
            temp_dict={"Username":self.user_cookie, "Source":chosen_stn1,"Destination": destination1, "Date":book_date}
            #res_cooki=json.dumps(str(self.user_cookie)+","+str(chosen_stn1)+","+str(destination1)+","+str(book_date))
            print('temp dict is :')
            print(temp_dict)
            # self.response.headers.add_header('Set-Cookie', 'Reservation=%s' % (res_cooki))
            #self.response.write('<meta http-equiv="refresh" content="0; url=/selectdep" />')
            # with open('reservation.json','w') as outputfile:
            #     json.dump(temp_dict,outputfile,indent=4,sort_keys=True)
            print('HIDDEN:::::::::::')
            print (destination1,book_date,chosen_stn1)
            self.cur.execute(statement16%(str(destination1),str(book_date),str(chosen_stn1))) #Setting the arrives at and departure date
            self.db.commit()
            
            #destination1=(destination.split(','))[1]
            print('Search String: %s' %(str(destination1)))
            self.cur.execute(statement13%(str(chosen_stn1),str(destination1))) #Storing train no into database
            self.db.commit()
            
            self.cur.execute(statement17) #searching for trains
            result=self.cur.fetchall()
            
            result=list(result)
            #self.response.write(SEARCH_TRAIN_PAGE)
            self.response.write('<h2 align="center"><b><font color="blue">Select Departure Page</font>  </b></h2>')
            self.response.write('<form action="/pngr_info" method="post">')
            self.response.write('<table style="width:60%" border="3">')
            self.response.write('<tr>')
            self.response.write('<th>Train</th>')
            self.response.write('<th>Duration</th>')
            self.response.write('<th>First Class Price</th>')
            self.response.write('<th>Second Class Price</th>')
            self.response.write('</tr>')
            for item in result:
                self.response.write('<tr>')
                #self.response.write('<td>')
                self.response.write('<td><b><font color="blue">%s</font> </b></td>' % str(item[0]))
                self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(item[1]))
                # self.response.write('<td><b><font color="green">$%s</font></b></td>' % str(item[2]))
                # self.response.write('<td>')
                track1=unicode(item[0])+","+unicode(item[1])+","+"first"+","+unicode(item[2])
                #track1=json.dumps(track1)
                # track1=unicode(track1)
                print track1
                track2=unicode(item[0])+","+unicode(item[1])+","+"second"+","+unicode(item[3])
                #track2=json.dumps(track2)
                # track2=unicode(track2)
                print track2
                
                # self.response.write('<td><h3><b>%s</b></h3><input type="submit" name="select" value="%s"><br>'% (str(item[2]),track1)) #track 1=trainno, duration,first class price
                # self.response.write('<td><h3><b>%s</b></h3><input type="submit" name="select" value="%s"><br>'% (str(item[3]),track2))#track 2=trainno, duration,second class price
                self.response.write('<td><button name="select" type="submit" value="%s">%s</button>'% (track1,str(item[2])))
                self.response.write('<td><button name="select" type="submit" value="%s">%s</button>'% (track2,str(item[3])))
                
                
                self.response.write('</td>')
                self.response.write('</tr>')
                self.response.write('<p></p>')
                           
                    
            
            self.response.write('</table>')
            #self.response.write('<input type="submit" value="Next">')
            # self.response.write('<div ><h2><b><font color="green">Current Total: $%s <font></b></h2></div>' %(total_cost))
            self.response.write('</form> ')
            
            
            self.db.commit()
class pngr_info(webapp2.RequestHandler):
    def post(self):
        # self.user_cookie=self.request.cookies.get('Reservation')
        # reservation_list=self.user_cookie.split(',')
        # print 'pngr page::::::::::'
        # print reservation_list
        
        
        # #-------------------------------------------------------------------------------------------
        # mykey = 'r2'
        # 
        # rsvn = g_reservation(parent=repository_key(mykey))
        # 
        # 
        # #[u'as', u'Fremont Station', u'Big Four Depot', u'2016-04-18']
        # 
        # rsvn.google_username = str(reservation_list[0])
        # #rsvn.google_train = str(reservation_list[1])
        # #rsvn.google_duration = str(reservation_list[2])
        # rsvn.google_departs = str(reservation_list[1])
        # rsvn.google_arrives = str(reservation_list[2])
        # rsvn.google_date=str(reservation_list[3])
        # #rsvn.google_class = str(reservation_list[0])
        # #rsvn.google_price = str(reservation_list[0])
        # #rsvn.google_bags = str(reservation_list[0])
        # #rsvn.google_psngrname = str(reservation_list[0])
        # 
        # 
        # 
        # 
        # # if(bool(rsvn.google_username) & bool(rsvn.google_departs) & bool(rsvn.google_arrives) & bool(rsvn.google_date)):  #Store if both fields are entered
        # #     book.put()
        # # else:
        # #     self.response.write('<h3><b><font color="red">INFO MISSING</font></b></h3>') #Error message when either field is not entered
        # #     self.response.write('<p></p>')
        #     #self.response.write('<a href=/enter> <h3 align="left"> Go back to enter book info page </h3> </a>')
            
        
        
        #----------------------------------------------------------------------------------------
        
        
        
        
        
        #self.user_cookie=self.request.cookies.get('Username')
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        
        price_select1=str(self.request.get('select'))
        price_select1=price_select1.split(',')
        print 'BUTTON OUTPUT:::::::::::::::::::'
        print price_select1
        # price_select2=str(self.request.get('second'))
        # price_select2=price_select2.split(',')
        # print price_select2
        
        if ('first' in price_select1):
            self.cur.execute(statement18%('First Class',price_select1[0])) #adding the class using train number as reference
            self.db.commit()
        elif ('second' in price_select1):
            self.cur.execute(statement18%('Second Class',price_select1[0]))
            self.db.commit()
        else:
            self.response.write('<h2><b>Please make a train selection</b></h2>')
        
        
        # if(bool(rsvn.google_username) & bool(rsvn.google_departs) & bool(rsvn.google_arrives) & bool(rsvn.google_date) & bool(rsvn.google_duration)):  #Store if both fields are entered
        #     tempkey=rsvn.put()
        #     print 'STORE SUCCESS !!!!!!!!!!!!!'
        # else:
        #     self.response.write('<h3><b><font color="red">INFO MISSING</font></b></h3>') #Error message when either field is not entered
        #     self.response.write('<p></p>')
        
        # res_cooki=reservation_list.append(price)
        # res_cooki=json.dumps(res_cooki)
        #self.response.headers.add_header('Set-Cookie', 'Reservation=%s' % (res_cooki))
        
        # self.response.write('<h3>Number of baggage :</h3><input type="number" step="1" name="bags" min="0" max="4" />')
        # #self.response.write('')
        # self.response.write('<p>Every passenger can bring upto 2 bags- 2 for free and 2 for $30 per bag</p>')
        self.response.write('''<form action="/finalreserve" method="post">
                                <div>
                                <label for="bags">Number of baggage: </label>
                                  <input type="number" step="1" min="0" max="4" name="bags" /> 
                                <p>Every passenger can bring upto 2 bags- 2 for free and 2 for $30 per bag</p>
                                  <label for="psngrname">Passenger Name:</label>
                                  <input type="text" name="psngrname" /> </div>
                                  <div class="button"><button type="submit">Next</button></div>
                              </form>''')
        
        
        #res_cooki=json.dumps(tempkey)
        # self.response.headers.add_header('Set-Cookie', 'impkey=%s' % (str(tempkey.id())))
        self.db.commit()
        
class finalreserve(webapp2.RequestHandler):
    def post(self):
        self.user_cookie=self.request.cookies.get('Username')
        
        # reservation_list=self.user_cookie.split(',')
        # print 'finalreserve page::::::::::'
        # print reservation_list
        #self.user_cookie=self.request.cookies.get('Username')

        
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        
        bags=self.request.get('bags')
        psngrname=self.request.get('psngrname')
        print bags
        print psngrname
        
        
        #------------------------------------------------------------------------------------------------------------------------------
        
        #nomeoncard,cardno,cvv,expdate
        
        nameoncard=str(self.request.get('nameoncard'))
        cardno=str(self.request.get('cardno'))
        cvv=str(self.request.get('cvv'))
        expdate=str(self.request.get('expdate'))
        delcard=str(self.request.get('delcard'))
        
        if (bool(nameoncard)==True and bool(cardno)==True and bool(cvv)==True and bool(expdate)==True):
            self.cur.execute(statement33%(cardno,cvv,expdate,nameoncard,str(self.user_cookie)) )
            self.db.commit()
        
        if bool(delcard)==True:
            t2=self.cur.execute(statement35 % (str(self.user_cookie)))
            self.db.commit()
            card_valid=self.cur.fetchall()
            print card_valid
            for i in card_valid:
                if delcard in i:
                    t2=self.cur.execute(statement36 % (str(delcard)))
                    self.db.commit()
                
        
        
        #------------------------------------------------------------------------------------------------------------------------------
        
        
        self.cur.execute(statement19%(str(psngrname),str(bags))) #adding the bags and passenger name
        self.db.commit()
        # nameofkey=str(self.request.cookies.get('impkey'))
        # print nameofkey
        # mykey=ndb.Key('Repository', =nameofkey)
        # #mykey = repository_key(nameofkey)
        # print mykey
        # 
        # rsvn = mykey.get()
        # rsvn.google_bags=bags
        # rsvn.google_psngrname=psngrname
        # if(bool(rsvn.google_bags) & bool(rsvn.google_psngrname) ):  #Store if both fields are entered
        #     rsvn.put()
        #     print 'STORE SUCCESS  AGAIN !!!!!!!!!!'
        # else:
        #     self.response.write('<h3><b><font color="red">INFO MISSING</font></b></h3>') #Error message when either field is not entered
        #     self.response.write('<p></p>')
        # 
        # 
        # 
        # 
        # rsvn_query = rsvn.query(ancestor=repository_key(mykey))
        # rsvns = rsvn_query.fetch(50)
        
        #print str(rsvns)
        
        t1=self.cur.execute(statement20) #fetching all trains in un-comitted reservation
        self.db.commit()
        train_list=self.cur.fetchall() 
        self.cur.execute(statement21)
        self.db.commit()
        durations=self.cur.fetchall()  #fetch all durations
        self.cur.execute(statement22)
        self.db.commit()
        prices=self.cur.fetchall()  #fetch the price
        self.cur.execute(statement23)
        self.db.commit()
        studentstatus=self.cur.fetchall() #fetch the whether student or not
        self.cur.execute(statement24)
        self.db.commit()
        place_details=self.cur.fetchall() #fetch the departs from,arrives at,class
        self.cur.execute(statement32)
        self.db.commit()
        bag_details=self.cur.fetchall() #fetch the bag and passenger name 
        
        print 'PLACE DETAILS:::::::::::::::::'
        print place_details
        
        
        
        
        #for each in rsvns:
        self.response.write('<form action="/finalreserve" method="post">')
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
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(durations[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][1]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(place_details[0][2]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(prices[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(bag_details[0][0]))
        self.response.write('<td><b><font color="blue">%s</font></b></td>' % str(bag_details[0][1]))
        
        self.response.write('<td>')
        
        self.response.write('<input type="radio" name="deltrain" value="delete"><br>')
        
        self.response.write('</td>')
        self.response.write('</tr>')
        self.response.write('<p></p>')
                       
                
        
        self.response.write('</table>')
        self.response.write('<input type="submit" value="Remove">')
        
        self.response.write('</form> ')
                       
        print ('student status is :::::::::::')
        print studentstatus[0][0]
        totalcost=0
        self.response.write('</table>')
        if studentstatus[0][0]==True:    
            self.response.write('<p><h3><b>Student discount applied</b><h3></p>')
            if int(bag_details[0][0])==3:
                totalcost=((int(prices[0][0])+30)*0.8)
            elif int(bag_details[0][0])==4:
                totalcost=((int(prices[0][0])+60)*0.8)
            else:
                totalcost=((int(prices[0][0])*0.8))
        elif studentstatus[0][0]==False:    
            self.response.write('<p><h3><b>Student discount NOT applied</b><h3></p>')
            if int(bag_details[0][0])==3:
                totalcost=((int(prices[0][0])+30))
            elif int(bag_details[0][0])==4:
                totalcost=((int(prices[0][0])+60))
            else:
                totalcost=((int(prices[0][0])))
        
        self.response.write('<h3><b>Total Cost : %s</b><h3>'%(totalcost))
        
        t1=self.cur.execute(statement27 % str(self.user_cookie))
        self.db.commit()
        card_nos=self.cur.fetchall()
        print ('CARD NOS:::::::::::::')
        print card_nos
        #To select card:
        self.response.write('<b><font color="blue">Select Card: </font>  </b>')
        self.response.write(' <form action="/confirmation" method="post">')
        # self.response.write('<input list="stations" name="station">')
        self.response.write('<select name="card">')
        for i in range(len(card_nos)):
            self.response.write('<option value="%s">%s</option>'%(str(card_nos[i][0]),str(card_nos[i][0])))

        self.response.write('</select>')
        
        self.response.write('<li> <a href=/paymentinfo> <h3>Add Card </h3></a>')
        self.response.write('<li> <a href=/makereserve> <h3>Continue adding a train</h3></a>')
        self.response.write('<input type="submit">')
        self.response.write('</form>')
        #self.response.write('<li> <a href=/givereview> <h3>Give review </h3></a>')
        
        
        
        self.db.commit()
            
class paymentinfo(webapp2.RequestHandler):
    def get(self):
        self.user_cookie=self.request.cookies.get('Username')   
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="r0cknr0lla",  # your password
                     db="phase3")        # name of the data base
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write('<h2 align="center"><b>Payment Information</b></h2>')
        self.response.write('<h2 align="center"><b>Add Card</b></h2>')
        self.response.write('''<body bgcolor="#ffc34d" >
                                
                                <form action="/finalreserve" method="post">
                                      <div>
                                        <label for="nameoncard">Name on card:</label>
                                        <input type="text" name="nameoncard" /> </div>
                                        <p></p>
                                        <label for="cardno">Card No:</label>
                                        <input type="text" name="cardno" /> 
                                        <p></p>
                                        <label for="cvv">CVV:</label>
                                        <input type="text" name="cvv" /> </div>
                                        <p></p>
                                    
                                        
                                         <input name="expdate" type="date" />
                                    <div class="button"><button type="submit">Add card</button></div>
                                    </form>
                                
                                
                                ''')
        self.response.write('<hr>')
        
        t2=self.cur.execute(statement34 % (str(self.user_cookie)))
        self.db.commit()
        del_number=self.cur.fetchall()
        print ('Del number is ::::::::')
        print del_number
        self.response.write('<h2 align="center"><b>Delete Card</b></h2>')
        self.response.write(' <form action="/finalreserve" method="post">')
        # self.response.write('<input list="stations" name="station">')
        self.response.write('<select name="delcard">')
        for i in range(len(del_number)):
            self.response.write('<option value="%s">%s</option>'%(str(del_number[i][0]),str(del_number[i][0])))

        self.response.write('</select>')

        self.response.write('<input type="submit">')
        self.response.write('</form>')
        

class confirmation(webapp2.RequestHandler):
    def post(self):
        self.user_cookie=self.request.cookies.get('Username')
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                 user="root",         # your username
                 passwd="r0cknr0lla",  # your password
                 db="phase3")        # name of the data base
        card_select=str(self.request.get('card'))
        
        self.cur = self.db.cursor()
        self.response.write(ALL_PAGE_HEADER)
        self.response.write('<h2 align="center"><b>Confirmation</b></h2>')
        t1=self.cur.execute(statement28 % str(card_select))
        self.db.commit()
        
        t2=self.cur.execute(statement29)
        self.db.commit()
        
        t3=self.cur.execute(statement30)
        self.db.commit()
        
        t4=self.cur.execute(statement31 % (str(self.user_cookie)))
        self.db.commit()
        conf_number=self.cur.fetchall()
        self.response.write('<h3 align="center"><b>Your confirmation number is : %s</b></h2>'%(str(conf_number[0][0])))
        
        
        
        