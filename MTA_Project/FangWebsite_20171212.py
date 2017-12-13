import cherrypy
import os, os.path

# "return" is to show on the web page something
#modeled on tutorial 6
class MTA_Notification(object):
    @cherrypy.expose
    def index(self):
      return """<html>
          <head>
              <title>Sign-up Page</title>
              <link href="/static/css/style.css" rel="stylesheet">      
          </head>
          <body><fieldset><legend>MTA Notification</legend>
          <form method="get" action="submit" target="_self"><h1>Sign up</h1><br/><p>Enter your email address here: <br>
             <input type="email" name="email" placeholder="Email address" id="email" required></p><p> When do you take MTA? Enter time in 24hr format: <br>
             <input type="text"  name="time" placeholder="HH:MM" pattern="([01]?[0-9]|2[0-3]):[0-5][0-9]" id="time" required></p><p><fieldset><legend>Please select all the possible lines you take: </legend>
                 <input type="checkbox" name="lines" value="123"/><lable for="123">1,2,3</lable><br />
                 <input type="checkbox" name="lines" value="456"/><label for="456">4,5,6</label><br />
                 <input type="checkbox" name="lines" value="7"/><label for="7">7</label><br />
                 <input type="checkbox" name="lines" value="ACE"/><label for="ACE">A,C,E</label><br />
                 <input type="checkbox" name="lines" value="BDFM"/><label for="BDFM">B,D,F,M</label><br />
                 <input type="checkbox" name="lines" value="G"/><label for="G">G</label><br />            
                 <input type="checkbox" name="lines" value="JZ"/><label for="JZ">J,Z</label><br />  
                 <input type="checkbox" name="lines" value="L"/><label for="L">L</label><br />
                 <input type="checkbox" name="lines" value="NQR"/><label for="NQR">N,Q,R</label><br />
                 <input type="checkbox" name="lines" value="S"/><label for="S">S</label><br />
                 <input type="checkbox" name="lines" value="SIR"/><label for="SIR">S,I,R</label><br /></fieldset><p>
             <button type="submit">submit your info</button></p>
            </form></fieldset>
           </body>
           <?php
           ?>
         </html>"""

    @cherrypy.expose
    def submit(self, email, time, lines):          # email is a string, time is a string, lines is a list
        lineChoice = ','.join(lines) 
        return "Your email is: " + email + "\nYour time of commute is: " + time + "\nYour lines of choice are: " + lineChoice

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(MTA_Notification(), '/', conf)
