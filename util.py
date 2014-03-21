import http.client

URL = """www.studentenwerk.uni-erlangen.de/verpflegung/de/sp-ingolstadt.shtml"""
def fetch():
	urlparts = URL.split('/')
	conn = http.client.HTTPConnection(urlparts[0])
	conn.request("GET",'/'+'/'.join(urlparts[1:]))
	response = conn.getresponse()
	data = response.read()
	return data
