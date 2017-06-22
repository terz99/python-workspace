# File import starts here
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cgi
import random
# File import ends here



# Session maker declaration starts here
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
# Session maker declaration ends here



class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
          	if self.path.endswith("/restaurants"):
          		self.send_response(200)
          		self.send_header("Content-type", "text/html")
          		self.end_headers()
          		output = ""
          		output += "<html><body>"
          		output += "<a href='/restaurants/new'>Add a new restaurant!</a><br/><br/>"

          		query_result = session.query(Restaurant.name, Restaurant.id).order_by(Restaurant.name).all()
          		for elem in query_result:
          			a = random.randint(0, 250)
          			b = random.randint(0, 250)
          			c = random.randint(0, 250)
          			output += "<div style='border-style:solid;border-color:red;padding:10px;background-color:rgb({},{},{});'>"\
          				.format(a, b, c)
          			output += "<h1>{}</h1>".format(elem.name)
          			output += "<a href='restaurants/{}/edit'>Edit</a>".format(elem.id)
          			output += "<br/>"
          			output += "<a href='/restaurants/{}/delete'>Delete</a>".format(elem.id)
          			output += "<br/>"
          			output += "</div>"

          		output += "</body></html>"

          		self.wfile.write(output)
          		print(output)
          		return
          	if self.path.endswith("/restaurants/new"):
          		self.send_response(200)
          		self.send_header("Content-type", "text/html")
          		self.end_headers()
          		output = ""
          		output += "<html><body>"
          		output += "<h1>Add a new restaurant!</h1>"
          		output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
          		output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>"
          		output += "<input type='submit' value='Create'>"
          		output += "</form></body></html>"
          		self.wfile.write(output)
          		return
          	if self.path.endswith("/edit"):
          		self.send_response(200)
          		self.send_header("Content-type", "text/html")
          		self.end_headers()

          		restaurant_id = int(self.path.split("/")[2])
          		query_result = session.query(Restaurant.name).filter_by(id=restaurant_id).first()
          		
          		output = ""
          		output += "<html><body>"
          		output += "<h2>{}</h2>".format(query_result.name)
          		output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/{}/edit'>".format(restaurant_id)
          		output += "<input name='renamedRestaurant' type='text' placeholder='Enter a new name'>"
          		output += "<input type='submit' value='Rename'>"
          		output += "</form></body></html>"
          		self.wfile.write(output)
          		return
          	if(self.path.endswith("/delete")):
          		self.send_response(200)
          		self.send_header("Content-type", "text/html")
          		self.end_headers()

          		restaurant_id = int(self.path.split("/")[2])
          		query_result = session.query(Restaurant).filter_by(id=restaurant_id).first()

          		output = ""
          		output += "<html><body>"
          		output += "<h1>Are you sure you want to delete '{}' restaurant?</h1>".format(query_result.name)
          		output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/{}/delete'>".format(restaurant_id)
          		output += "<input type='submit' value='Delete'>"
          		output += "</form></body></html>"

          		self.wfile.write(output)
          		return



        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:

        	if self.path.endswith("/restaurants/new"):

        		ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
        		if ctype == "multipart/form-data":
        			fields = cgi.parse_multipart(self.rfile, pdict)
        			messagecontent = fields.get("newRestaurantName")

        		new_restaurant = Restaurant(name=messagecontent[0])
        		session.add(new_restaurant)
        		session.commit()

        		self.send_response(301)
        		self.send_header("Content-type", "text/html")
        		self.send_header("Location", "/restaurants")
        		self.end_headers()
        		return
        	if self.path.endswith("/edit"):

        		ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
        		if ctype == "multipart/form-data":
        			fields = cgi.parse_multipart(self.rfile, pdict)
        			messagecontent = fields.get("renamedRestaurant")

        			restaurant_id = int(self.path.split("/")[2])
        			query_result = session.query(Restaurant).filter_by(id=restaurant_id).first()
        			query_result.name = messagecontent[0]
        			session.add(query_result)
        			session.commit()
        			self.send_response(301)
        			self.send_header("Content-type", "text/html")
        			self.send_header("Location", "/restaurants")
        			self.end_headers()

    			return
    		if self.path.endswith("/delete"):
    			ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
    			if(ctype == 'multipart/form-data'):
					restaurant_id = int(self.path.split("/")[2])
					query_result = session.query(Restaurant).filter_by(id=restaurant_id).first()
					session.delete(query_result)
					session.commit()
					self.send_response(301)
					self.send_header("Content-type", "text/html")
					self.send_header("Location", "/restaurants")
					self.end_headers()


        except:
            pass

def main():


	try:

		port = 8080
		server = HTTPServer(("", port), webserverHandler)
		print("Web server running on port {}".format(port))
		server.serve_forever()

	except KeyboardInterrupt:
		print("^C entered, stopping web server...")
		server.socket.close()

if __name__ == "__main__":
	main()