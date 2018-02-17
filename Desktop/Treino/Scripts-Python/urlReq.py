import urllib.parse
import urllib.request



url = 'http://localhost/fale-conosco.html'

values = {'cNome' : 'Michael Foord',
      	  'cMail' : 'Northampton@dot'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
try: req = urllib.request.Request(url,data)
except urllib.error.URLError as e:
	print(e.reason)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)