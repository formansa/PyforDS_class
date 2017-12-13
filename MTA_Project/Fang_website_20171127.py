import cherrypy
import os, os.path

class NYCommuter(object):

    @cherrypy.expose
    def userInput(self):
      return """<html>
        <head>
		    <title>Commute Info</title>
		    </head>
		    <body>
		    <form method="get" action="record">
		      <h1>Sign up</h1><br/>
          <p>
            <input type="text" placeholder="Full name" name="name"></p>
		      <p>
		        <input type="email" placeholder="Email address" name="email"></p>
		      <p>
		        <input type="time" name= "time"></p>
		      <p>
		        <label for="lines">What line do you take?</label>
                <select name="lines" id="Lines">
                   <option value="123">1,2,3</option> 
                   <option value="456">4,5,6</option> 
                   <option value="7">7</option> 
                   <option value="ACE">A,C,E</option>
                   <option value="BDFM">B,D,F,M</option>
                   <option value="G">G</option>
                   <option value="JZ">J,Z</option>
                   <option value="L">L</option>
                   <option value="NQR">N,Q,R</option>
                   <option value="S">S</option>
                   <option value="SIR">SIR</option>
                </select>
		      <p>
		        <button type="submit">Submit your info</button></p>
		    </form>
		  </body>
	    </html>"""

    def record(self, name, email, time, lines):
       user= {'name': "name", 'email': "email", 'time' = time, 'lines'="lines"}
       return user

    @cherrypy.expose
       return user


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
    cherrypy.quickstart(NYCommuter(), '/', conf)