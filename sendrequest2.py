import urllib
import urllib2 
import time
#from poster.encode import multipart_encode
#from poster.streaminghttp import register_openers
import requests

url = 'http://shubhagrawal.in/agv_new1.php?'
files = {'file': open('image.jpeg', 'rb')}
r = requests.post(url, files=files)
'''
while True:
#	register_openers()
#	datagen, headers = multipart_encode({"file[]" : open("D:\hedef\myfile.jpg","rb"),"content_type":"1","thumb_size":"350"})
	url = 'http://shubhagrawal.in/agv_new.php?'
	rq = ""
	rq = url + 'lati=' + '53.25' + '&longi=' + '29' + '&speed=' + '0' + '&heading=' + '0' + '&gearposition=' + '0' + '&brakeposition=' + '0' + '&mode=' + '0'  
	imgfile = open("image.jpg", "rb")
    urllib.urlopen("http://www.example.com/", imgfile.read())
	req = urllib2.Request(rq)
	response = urllib2.urlopen(req)
	print response
	time.sleep(1)
'''
