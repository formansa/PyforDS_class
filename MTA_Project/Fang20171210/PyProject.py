import cherrypy
import os, os.path
import pandas as pd

def init():
  data=pd.DataFrame(index=['User','Time','123','456','7','ACE','BDFM','G','JZ','L','NQR','S','SIR'],dtype=str)
  return data
'''
import sqlite3

DB_STRING = "UserData.db"
'''

class MTA_Signup(object):
    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def index(self):
      return open('index.html')

@cherrypy.expose
class MTA_Notification(object):

    def addProfile(data,email,time,lines):
      l=[email,time]    
      line=binaryConverter(lines)
      for i in line:
          l.append(i)
      try:
          col=max(data.columns)+1
      except ValueError:
          col=0
      data[col]=l

'''
def setup_database():
    # Create table 'entries' in the database on server startup
    with sqlite3.connect(DB_STRING) as con:
       con.execute(''CREATE TABLE entries
        (user text, commuteTime time, '123' text, '456' text, '7' text, 'ACE' text, 'BDFM' text, 'G' text, 'JZ' text, 'L' text, 'NQR' text, 'S' text, 'SIR' text )')

def save_database():
    # save (commit) the changes and close the connection
    with sqlite3.connect(DB_STRING) as con:
       con.commit()
       con.close()
'''

# # Function to encode a list of lines as a list of bits, based on the alllines table

# In[12]:

def binaryConverter(line):
  l=alllines[:]
  for i in range(len(l)):
      if l[i] in line:
          l[i]=1
      else:
          l[i]=0
  return l

def binaryDecoder(line):
  s=[]
  for i in range(len(line)):
      if line[i]==1:
          s.append(alllines[i])
  return s



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = MTA_Signup()
    webapp.userInput = MTA_Notification()
    cherrypy.quickstart(webapp, '/', conf)