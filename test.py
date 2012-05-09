import urllib2
# 
# import socket
# def renewTorIdentity():
#  success = False
#  s = socket.socket()
#  s.connect(('localhost', 9051))
#  s.send("AUTHENTICATE\r\n")
#  resp = s.recv(1024)
#  if resp.startswith('250'):
#   s.send("signal NEWNYM\r\n")
#   resp2 = s.recv(1024)
#   if resp2.startswith('250'):
#    success = True
#  return success

# 
# proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8080"})
# opener = urllib2.build_opener(proxy_support) 
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# print opener.open('http://www.google.com').read()
# 
# # 
# url = "http://www.google.com"
# proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8080"})
# opener = urllib2.build_opener(proxy_support)
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# response = opener.open(url).read()
# print response



# # using TOR !
# proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"} )
# opener = urllib2.build_opener(proxy_support)
# urllib2.install_opener(opener)
# # every urlopen connection will then use the TOR proxy like this one :
# urllib2.urlopen('http://www.google.fr').read()
# # and to renew my route when i need to change the IP :
# print "Renewing tor route wait a bit for 5 seconds"
# from TorCtl import TorCtl
# conn = TorCtl.connect(passphrase="lol")
# conn.sendAndRecv('signal newnym\r\n')
# conn.close()
# import time
# time.sleep(5)
# print "renewed"

proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
opener = urllib2.build_opener(proxy_support) 
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
print opener.open('http://www.google.com').read()




