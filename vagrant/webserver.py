from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#from http.server import BaseHTTPRequestHandler, HTTPServer




# what code to execute, based on type of request
class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>Hello!</body></html>"
				self.wfile.write(output)
				print(output)
				return

		except IOError:
			self.send_error(404, "File not Found {}").format(self.path)



# instantiate server, what port it listens on
def main():
	try:
		port = 8080
		server = HTTPServer(('',port), webserverHandler)
		print("Web server running on port {}").format(port)
		#constantly listening until KeyboardInterrupt(ctrl+c)
		server.serve_forever()

	except KeyboardInterrupt:
		print(" ^C entered, stopping web server ...")
		server.socket.close()


if __name__ == '__main__':
	main()