import rospy
from std_msgs.msg import String 
import time 
import urllib
import urllib2
import datetime
import thread
import csv

output1 = '0' 
output2 = '0' 
output3 = '0' 
output4 = '0' 
output5 = '0' 

def callback1(data):
	global output1
	output1 = data.data

def callback2(data):
	global output2
	output2 = data.data

def callback3(data):
	global output3
	output3 = data.data

def callback4(data):
	global output4
	output4 = data.data

def callback5(data):
	global output5
	output5 = data.data
        
def  listener():
	rospy.init_node('listener',anonymous = True)
	rospy.Subscriber("chatter1", String, callback1)
	rospy.Subscriber("chatter2", String, callback2)
	rospy.Subscriber("chatter3", String, callback3)
	rospy.Subscriber("chatter4", String, callback4)
	rospy.Subscriber("chatter5", String, callback5)
	rospy.spin()
def url_send() :
	global output1  
	global output2  
	global output3  
	global output4  
	global output5 
	fname = datetime.datetime.now()
	with open(str(fname)+'.csv','wb') as csvfile:
		writer= csv.writer(csvfile , delimeter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['time', 'lati', 'longi', 'speed', 'heading', 'gearposition'])
		while True:
			try:
				url = 'http://shubhagrawal.in/agv_new.php?'
				rq = ""
				rq = url + 'lati=' + output1 + '&longi=' + output2 + '&speed=' + output3 + '&heading=' + output4 + '&gearposition=' + output5 + '&brakeposition=' + '0' + '&mode=' + '0'  
				req = urllib2.Request(rq)
				response = urllib2.urlopen(req)
				now=datetime.datetime.now()
				print response
				writer.writerow([now.isoformat(), output1, output2, output3, output4, output5])
				time.sleep(1)
			except httplib.BadStatusLine:
				pass
if __name__ == '__main__' :
	thread.start_new_thread( url_send , ())
	listener()	

