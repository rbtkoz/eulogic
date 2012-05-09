import urllib2
import simplejson
import re
import requests
from bs4 import BeautifulSoup
from random import choice


# The request also includes the userip parameter which provides the end
# user's IP address. Doing so will help distinguish this legitimate
# server-side traffic from traffic which doesn't come from an end-user.

id = "hotdog"  # dynamic id from site
url = ('https://ajax.googleapis.com/ajax/services/search/web'
       '?v=1.0&q='+ id + '&userip=USERS-IP-ADDRESS')

request = urllib2.Request(url, None, {'Referer': "www.google.com" })
response = urllib2.urlopen(request)  # opening url

								# Process the JSON string.
results = simplejson.load(response)
results = results["responseData"]
results = results['cursor']
results = results["moreResultsUrl"]
print results

								#results = results['resultCount']

								#regex to add number to results
split = re.split("start=0", results)
newurl= split[0] + "start=100" +split[1]
print "found!!!"+ newurl 

r = requests.get(newurl)
								# print r.status_code
								# print r.headers['content-type']
r= r.text
soup = BeautifulSoup(r)

all=[]
for link in soup.find_all("a"):
  	all.append(link.get("href"))

for s in all:
	if re.findall("/url?", s):
		
		split1 = re.split("&", s)	
		split2 =re.split("=", split1[0])
		death = (split2)[1].split('/n')
		deathlinks = []
		for d in death:
			do = d.split()
			# str(do)
			# 			print type(do)
			myString = ",".join(do)
			print type(myString)
			# deathlinks.append(d.split('\n')[0])
			# 			print deathlinks[1]
			# 			
			# 			data = [death.strip().split(':') for line in d.split('\n') if line.strip()]
			# 						# 
						# one = d.split('h')[0]
						# print one[1]	
						# 		
		# deathlinks=[]
		# 	
		# 	for s in death:
		# 		deathlinks.append(s)
		# 		print deathlinks[0]
		# 	
		# 
		# sp =(split2[1])
		# 	
		# 
		# print (sp[0](1))
		# 
		
		# for s in split2[1]:
		# 		urly.append(s)
		# 	print urly	
		# urly.append(split2[1])
		# 		for s in urly:
		# 			print s[1]
			
			# deathlinks.append(s)
			# print deathlinks[1]
			
		# deathlinks.append(split2[1])
		# print len.deathlinks
			# print choice(deathlinks)
# if b:
# 	print b()	
# parse= re.match("http", str(all))
# print parse
# 

# soup.find_all('a')
# soup = BeautifulSoup("<a href>data</a>")
# 











# f = urllib2.urlopen(newurl)
# Read from the object, storing the page's contents in 's'.
# s = f.read()
# f.close()
# print s
# 
# newsearch = urllib2.urlopen(newurl)
# 
# newresult = simplejson.load(newsearch)
# print newresult
#open new link
# newsearch= urllib2.Request(newurl, None, {'Referer': "www.google.com"})
# newresponse = urllib2.urlopen(newsearch)
# newresult = simplejson.load(newresponse)
# print newresult

# curl --user-agent "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)" "http://www.google.com/search?oe=utf8&ie=utf8&source=uds&start=100&hl=en&q=hotdog"








# for result in results:
# 	print result[-1]
	
# now have some fun with the results...


# https://www.google.com/#q="searchterm"&hl=en&prmd=imvnsol&ei=sguYT43JDYme6AHTgqXkBg&start=800&sa=N&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=8c09eaea2875d914&biw=1680&bih=885





# eturn result['ResultSet']
# Usage of the above:
# >>> info = search('json python')
# >>> info['totalResultsReturned']
# 20
# >>> info['totalResultsAvailable']
# u'212000'
# >>> info['firstResultPosition']
# 1
# >>> results = info['Result']
# >>> for result in results:
# ...     print result['Title'], result['Url']
# Python Stuff http://undefined.org/python/
# SourceForge.net: json-py https://sourceforge.net/projects/json- py
# Introducing JSON http://www.json.org/
# ...
# Each result is a Python dictionary containing a number of keys. The full dictionary for a result looks like this:
# >>> from pprint import pprint
# >>> pprint(results[0])
# {u'Cache': {u'Size': u'22237',
#             u'Url': u'http://216.109.125.130/search/cache... '},
#  u'ClickUrl': u'http://undefined.org/python/#simple_ json',
#  u'DisplayUrl': u'undefined.org/python/#simple_json',
#  u'MimeType': u'text/html',
#  u'ModificationDate': 1150786800,
#  u'Summary': u'... Python Stuff. Support the development of py2app, xattr ...',
#  u'Title': u'Python Stuff',
#  u'Url': u'http://undefined.org/python/#simple_ json'}