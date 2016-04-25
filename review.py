
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

class view_review(webapp2.RequestHandler):
    def get(self):
         
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        
        self.cur.execute(statement57)
        trainnos=self.cur.fetchall()
        
        self.response.write('<h2 align="center"><b><font color="blue">View Review</font>  </b></h2>')
        self.response.write(' <form action="/viewreview2" method="post">')
        self.response.write('<h3><b>Select Train Number</b></h3>')
        
        self.response.write('<select name="trainno">')
        for i in range(len(trainnos)):
            self.response.write('<option value="%s">%s</option>'%(str(trainnos[i][0]),str(trainnos[i][0])))

        self.response.write('</select>')
        self.response.write('<input type="submit">')
        self.response.write('</form>')

class view_review2(webapp2.RequestHandler):
    def post(self):
         
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        trainno=str(self.request.get('trainno'))
        self.cur.execute(statement58 % (trainno))
        reviews=self.cur.fetchall()
        self.db.commit()
        
        self.response.write('<h2><b><font color="blue">Reviews for train no %s</font></b><h2>' % str(trainno))
        self.response.write('<table style="width:60%" border="3">')
        self.response.write('<tr>')
        # self.response.write('<th>Train No</th>')
        self.response.write('<th>Rating</th>')
        self.response.write('<th>No. of reviews</th>')
        self.response.write('<th>Comment</th>')

        self.response.write('</tr>')
        
        
        for i in range(len(reviews)):
            #self.response.write('<table style="width:100%">')
            self.response.write('<tr>')
            #self.response.write('<td>')

            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(reviews[i][0])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(reviews[i][1])))
            self.response.write('<td><b><font color="blue">%s</font></b></td>' % (str(reviews[i][2])))

            
            self.response.write('</tr>')
            self.response.write('<p></p>')
        self.response.write('<li> <a href=/menu> <h3>Back to choose functionality</h3></a>')
        
        
class give_review(webapp2.RequestHandler):
    def get(self):
         
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        
        self.cur.execute(statement57)
        trainnos=self.cur.fetchall()
        self.db.commit()
        options=["Very Good","Good","Neutral","Bad", "Very Bad"]
        self.response.write('<h2 align="center"><b><font color="blue">Give Review</font>  </b></h2>')
        self.response.write(' <form action="/givereview2" method="post">')
        self.response.write('<h3><b>Select Train Number:</b></h3>')
        
        self.response.write('<select name="trainno" required>')
        for i in range(len(trainnos)):
            self.response.write('<option value="%s" >%s</option>'%(str(trainnos[i][0]),str(trainnos[i][0])))
        
        
        self.response.write('</select>')
        
        self.response.write('<p></p>')
        self.response.write('<p></p>')
        self.response.write('<h3><b>Rating:</b></h3>')
        self.response.write('<select name="rating" required>')
        for i in range(len(options)):
            self.response.write('<option value="%s">%s</option>'%(str(options[i]),str(options[i])))

        self.response.write('</select>')
        
        self.response.write('''<p></p>
                                <label for="comment">Comment: </label>
                                <input type="text" name="comment" /> </div>
                                <p></p>''')
        self.response.write('<input type="submit">')
        self.response.write('</form>')

class give_review2(webapp2.RequestHandler):
    def post(self):
         
        self.response.write(ALL_PAGE_HEADER)
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="r0cknr0lla",  # your password
                             db="phase3")        # name of the data base
        self.user_cookie=str(self.request.cookies.get('Username'))

        self.cur = self.db.cursor()
        trainno=str(self.request.get('trainno'))
        #self.cur.execute(statement58 % (trainno))
        #reviews=self.cur.fetchall()
        rating=str(self.request.get('rating'))
        #self.cur.execute(statement58 % (trainno))
        comment=str(self.request.get('comment'))

        self.cur.execute(statement60 % (str(trainno),str(rating),str(comment),self.user_cookie))
        self.db.commit()
        
        
        self.response.write('<h2><b><font color="blue">Review has been recorded</font></b><h2>')
        