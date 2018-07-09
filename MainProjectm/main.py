import RPi.GPIO as GPIO
import thread
import threading
import time
import os
from subprocess import call
import numpy as np
import cv2
from datetime import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from getpass import getpass
from stat import *
from getpass import getpass
from stat import *
import socket
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
import urllib2
import cookielib
class Master(object):
    #Write Function
    #Sending data topt the server
    @staticmethod
    def sendtoserver(message):
        try:
            TCP_IP = '192.168.43.195'
            TCP_PORT = 8888
            BUFFER_SIZE = 1000
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(message)
            stat=s.recv(BUFFER_SIZE)
            s.close()
        except:
            stat="TCP ERROR"
        return stat
    @staticmethod
    def writeto(pstat):
        f = open("data.txt",'w')
        f.write(pstat)
        f.close()
    @staticmethod
    def tcpmsg():
        global camera_status,flame_status,mail_status,sms_status
        global alert_tcp, status_tcp
        s='0000000000000000'
        z=4
        x=0
        if (os.stat("tcpmsg.txt").st_size != 0):
        # Read lines in file
            line = []
            f2 = open('tcpmsg.txt', 'r')
            with f2 as f:
                for lines in f:
                    lines = lines.strip()  # or some other preprocessing
                    # print "In File:"+lines
                    line.append(lines)
                    s = line[0]
                f2.close()
        camera_status = int(s[0])
        flame_status = int(s[1])
        mail_status = int(s[2])
        sms_status = int(s[3])
        while(z<16):
            alert_tcp[x]=int(s[z])
            status_tcp[x]=int(s[z+1])
            z+=2
            x+=1
        print str(camera_status)+" "+str(flame_status)+" "+str(mail_status)+" "+str(sms_status)
        print alert_tcp
        print status_tcp
    @staticmethod
    #send SMS********************************************************************
    def smsmessage(m):
            number = "1111111111"
            message=m
            username = "0000000000"
            passwd = "xxxxxxxx"

            message = "+".join(message.split(' '))

            #loggin
            url ='http://site24.way2sms.com/Login1.action?'
            data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
            cj= cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
            try:
                usock =opener.open(url, data)
            except IOError:
                print "URL error"
                #return()

            """jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
            send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
            opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
            try:
                sms_sent_page = opener.open(send_sms_url,send_sms_data)
                print "message sent"
            except IOError:
                print "mesage error" """

            jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
            send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
            opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
            try:
                sms_sent_page = opener.open(send_sms_url,send_sms_data)
                print "message sent"
            except IOError:
                print "message error" 
                
 
   
               
            
            
    @staticmethod   
    def RunClient():
         client.connec()


    def appendan(self,an,al,st): 
            tup1.append(an)
            tup2.append(al)
            tup3.append(st)
    def clean(self):
            tup1=[]
            tup2=[]
            tup3=[]
    def  dummy(self):
            #print cam,flame,mail,sms,tup1,tup2,tup3
            #while(flame!=0):
               print "fire",cam
#SendMail*******************************************************************
    @staticmethod
    def emailfunc(z):
        #No gmail since it blocks the script
        gmail_user = "kbc@outlook.com" #our mail
        gmail_pwd = "kbc123"
        to = "kkk@hotmail.com" #user mail
        subject = "Security Breach"
        text =z
        """cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap = cv2.VideoCapture(0)
        print "Saving Photo"
        picname = datetime.now().strftime("%y-%m-%d-%H-%M")
        picname = picname+'.jpg'
        cv2.imwrite(picname, frame)
        print "Sending email"
            
        attach = picname"""
            
        msg = MIMEMultipart()

        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        mailServer = smtplib.SMTP("smtp.live.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        # Should be mailServer.quit(), but that crashes...
        mailServer.close()
        print "Email Sent"
        #os.remove(picname)


if __name__=="__main__":
    camera_status,flame_status,mail_status,sms_status=0,0,0,0
    alert_tcp = [0,0,0,0,0,0]
    status_tcp = [0,0,0,0,0,0]
    m=Master()
    count=[0,0,0,0,0,0,0,0]
    #cl=threading.Thread(name='Cli',target=m.RunClient)
    #cl.start()
    m.tcpmsg()
    while True:
        time.sleep(0.3)
        if(camera_status==1):
           # print count
            i=GPIO.input(11)
            if i==0:
                count.pop(0)
                count.append(0)
                #print "No movement detected"
                GPIO.output(3,0)
                if(sum(count)==0):
                    #print count
                    m.writeto("0")
                    print "0"
                #m.writeto("0")
                
            elif i==1:
                #print "Movement detected"
                GPIO.output(3,1)
                count.pop(0)
                #print "Movement detected"
                count.append(1)
                if(sum(count)!=0):
                    #print count
                    m.writeto("1")
                    print "1"
                    #m.cameradetect(tup2,tup3)
                    #print "will go to cam func"
        if(flame_status==1):
            j=GPIO.input(13)
            if j==1:
                #print "no fire"
                GPIO.output(3,0)
            elif j==0:
                print 'Fire detected.'
                tcp_msg="11000"+str(camera_status)+str(flame_status)+str(mail_status)+str(sms_status)
                print(m.sendtoserver(tcp_msg))
                if(sms_status==1):
                    m.smsmessage("ALERT! FIRE DETECTED")
                if(mail_status==1):
                    m.emailfunc("ALERT! FIRE DETECTED")
