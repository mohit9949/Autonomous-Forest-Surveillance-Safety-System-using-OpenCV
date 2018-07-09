import urllib2
import cookielib
import time
import datetime
from getpass import getpass
from stat import *
from subprocess import call
import numpy as np
import cv2
from datetime import datetime
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import socket

statuses_tcp =[0,0,0,0]
alert_tcp = [0,0,0,0,0,0]
status_tcp = [0,0,0,0,0,0]

#Sending data topt the server
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
    
#Get TCP Message commands
def tcpmsg():
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
    statuses_tcp[0] = int(s[0])
    statuses_tcp[1] = int(s[1])
    statuses_tcp[2] = int(s[2])
    statuses_tcp[3] = int(s[3])
    while(z<16):
        alert_tcp[x]=int(s[z])
        status_tcp[x]=int(s[z+1])
        z+=2
        x+=1

#send Email
def sendemail(mail_status,maxnum,message):
    if(mail_status==1):
        
        gmail_user = "kbc@outlook.com" #our mail
        gmail_pwd = "kbc123"
        to = "kkk@hotmail.com"  # user mail
        subject = "Security Breach"
        msg = MIMEMultipart()
        print "Sending email"
        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        if(maxnum[0]>0):
             picname1="human.jpg"
             attach1=picname1
             part1 = MIMEBase('application', 'octet-stream')
             part1.set_payload(open(attach1, 'rb').read())
             Encoders.encode_base64(part1)
             part1.add_header('Content-Disposition',
                            'attachment; filename="%s"' % os.path.basename(attach1))
             msg.attach(part1)
        if(maxnum[1]>0):
            picname1 = "tiger.jpg"
            attach1 = picname1
            part1 = MIMEBase('application', 'octet-stream')
            part1.set_payload(open(attach1, 'rb').read())
            Encoders.encode_base64(part1)
            part1.add_header('Content-Disposition',
                             'attachment; filename="%s"' % os.path.basename(attach1))
            msg.attach(part1)
        if (maxnum[2] > 0):
            picname1 = "rhino.jpg"
            attach1 = picname1
            part1 = MIMEBase('application', 'octet-stream')
            part1.set_payload(open(attach1, 'rb').read())
            Encoders.encode_base64(part1)
            part1.add_header('Content-Disposition',
                             'attachment; filename="%s"' % os.path.basename(attach1))
            msg.attach(part1)
        if (maxnum[3] > 0):
            picname1 = "bear.jpg"
            attach1 = picname1
            part1 = MIMEBase('application', 'octet-stream')
            part1.set_payload(open(attach1, 'rb').read())
            Encoders.encode_base64(part1)
            part1.add_header('Content-Disposition',
                             'attachment; filename="%s"' % os.path.basename(attach1))
            msg.attach(part1)
        if (maxnum[4] > 0):
            picname1 = "lion.jpg"
            attach1 = picname1
            part1 = MIMEBase('application', 'octet-stream')
            part1.set_payload(open(attach1, 'rb').read())
            Encoders.encode_base64(part1)
            part1.add_header('Content-Disposition',
                             'attachment; filename="%s"' % os.path.basename(attach1))
            msg.attach(part1)
        if (maxnum[5] > 0):
            picname1 = "cat.jpg"
            attach1 = picname1
            part1 = MIMEBase('application', 'octet-stream')
            part1.set_payload(open(attach1, 'rb').read())
            Encoders.encode_base64(part1)
            part1.add_header('Content-Disposition',
                             'attachment; filename="%s"' % os.path.basename(attach1))
            msg.attach(part1)
        mailServer = smtplib.SMTP("smtp.live.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        # Should be mailServer.quit(), but that crashes...
        mailServer.close()
        print "Email Sent"
    else:
        print 'mail_status='+str(mail_status)
        print "Email Disabled!"
        
#send SMS
def sendsms(sms_status,message):
    if(sms_status==1):
        number = "1111111111"
        #message = m
        username = "0000000000
        passwd = "123456789"

        #message = "+".join(message.split(' '))

        # loggin
        url = 'http://site24.way2sms.com/Login1.action?'
        data = 'username=' + username + '&password=' + passwd + '&Submit=Sign+in'
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            usock = opener.open(url, data)
        except IOError:
            print "URL error"
            # return()

        """jession_id =str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
            print "message sent"
        except IOError:
            print "mesage error" """

        jession_id = str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token=' + jession_id + '&mobile=' + number + '&message=' + message + '&msgLen=136'
        opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url, send_sms_data)
            print "message sent"
        except IOError:
            print "message error"
    else:
        print "SMS Disabled!"
#Read PIR Data
def readPIR():
    s='0'
    if (os.stat("data.txt").st_size != 0):
        # Read lines in file
        line = []
        f2 = open('data.txt', 'r')
        with f2 as f:
            for lines in f:
                lines = lines.strip()  # or some other preprocessing
                # print "In File:"+lines
                line.append(lines)
                s = line[0]
            f2.close()
    return s

def alert_func(maxnum, status,mail_status,sms_status):
        message = "ALERT!\n"
        smsmessage="ALERT! "
        if (maxnum[0] > 0 and status[0] >= 1):
            message += str(maxnum[0]) + " intruder(s) detected\n"
            tcp_message="101"+str(maxnum[0])+str(status[0])+str(statuses_tcp[0])+str(statuses_tcp[1])+str(statuses_tcp[2])+str(statuses_tcp[3])
            print(sendtoserver(tcp_message))
            if(status[0]==3):
                smsmessage+=str(maxnum[0] )+ " intruder(s), "
        if (maxnum[1] > 0 and status[1] >= 1):
            message += str(maxnum[1] )+ " tigers(s) detected\n"
            tcp_message="1"+"0"+"2"+str(maxnum[1])+str(status[1])+str(statuses_tcp[0])+str(statuses_tcp[1])+str(statuses_tcp[2])+str(statuses_tcp[3])
            print(tcp_message)
            print(sendtoserver(tcp_message))
            if (status[1] == 3):
                smsmessage =str(maxnum[1]) + " tiger(s), "
        if (maxnum[2] > 0 and status[2] >= 1):
            message += str(maxnum[2]) + " rhino(s) detected\n"
            tcp_message="1"+"0"+"3"+str(maxnum[2])+str(status[2])+str(statuses_tcp[0])+str(statuses_tcp[1])+str(statuses_tcp[2])+str(statuses_tcp[3])
            print(sendtoserver(tcp_message))
            if (status[2] == 3):
                smsmessage = str(maxnum[2]) + " rhino(s), "
        if (maxnum[3] > 0 and status[3] >= 1):
            message += str(maxnum[3]) + " bear(s) detected\n"
            tcp_message="1"+"0"+"4"+str(maxnum[3])+str(status[3])+str(statuses_tcp[0])+str(statuses_tcp[1])+str(statuses_tcp[2])+str(statuses_tcp[3])
            print(sendtoserver(tcp_message))
            if (status[3] == 3):
                smsmessage = str(maxnum[3]) + " bear(s), "
        if (maxnum[4] > 0 and status[4] >= 1):
            message += str(maxnum[4]) + " lion(s) detected\n"
            tcp_message="1"+"0"+"5"+str(maxnum[4])+str(status[4])+str(statuses_tcp[0])+str(statuses_tcp[1])+str(statuses_tcp[2])+str(statuses_tcp[3])
            print(sendtoserver(tcp_message))
            if (status[4] == 3):
                smsmessage =str( maxnum[4]) + " lion(s), "
        if (maxnum[5] > 0 and status[5] >= 1):
            message +=str( maxnum[5]) + " cat(s) detected\n"
            tcp_message="1"+"0"+"6"+str(maxnum[5])+str(status[5])+str(statuses_tcp[0])+str(statuses_tcp[1])+str(statuses_tcp[2])+str(statuses_tcp[3])
            print(sendtoserver(tcp_message))
            if (status[5] == 3):
                smsmessage = str(maxnum[5]) + " cats(s), "
        if(smsmessage!='ALERT! '):
            smsmessage+="detected."
            sendsms(sms_status,smsmessage)
        if(message!='ALERT!\n'):
            sendemail(mail_status,maxnum,message)

                  #alert, status
def cameraditection(tup1,tup2,mail_status,sms_status):
    maxh=0
    maxt=0
    maxr=0
    maxl=0
    maxb=0
    maxc=0
    tuph = [0, 0, 0]
    tupt = [0, 0, 0]
    tupr = [0, 0, 0, 0]
    tupb = [0, 0, 0]
    tupl = [0, 0, 0,0,0,0]
    tupc = [0, 0, 0]
    if(tup2[0]==1):
        human_cascade=cv2.CascadeClassifier('/home/pi/Desktop/MainProjectm/GoodCascades/human.xml')
    if(tup2[1]==1):
        tiger_cascade=cv2.CascadeClassifier("/home/pi/Desktop/MainProjectm/GoodCascades/qtiger.xml")
    if (tup2[2] == 1):
        rhino_cascade = cv2.CascadeClassifier("/home/pi/Desktop/MainProjectm/GoodCascades/qrhino20.xml")
    if (tup2[3] == 1):
        bear_cascade = cv2.CascadeClassifier("/home/pi/Desktop/MainProjectm/GoodCascades/qbear.xml")
    if (tup2[4] == 1):
        lion_cascade = cv2.CascadeClassifier("/home/pi/Desktop/MainProjectm/GoodCascades/qlion20.xml")
    if (tup2[5] == 1):
        cat_cascade = cv2.CascadeClassifier("/home/pi/Desktop/MainProjectm/GoodCascades/qcat.xml")
    cap=cv2.VideoCapture(0)
    lt = []
    yu=1
    timestr= "/home/pi/Desktop/MainProjectm/Video Logs/"
    timestr += time.strftime("%Y%m%d-%H%M%S")
    timestr+='.avi'
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter(timestr, fourcc, 20.0, (640,480))
    while True:
        yu+=1
        human=[]
        lion=[]
        tiger=[]
        bear=[]
        cat=[]
        rhino=[]
        counter=0
        if(int(readPIR())==0):
            break
        ret,img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if(counter<=5000):
                counter+=1
                out.write(img)
                #cv2.imshow('frame',frame)
        if(tup2[0]==1):
            human=human_cascade.detectMultiScale(gray,1.3,5)
            lt.append(human)
            tuph.append(len(human))
            tuph.pop(0)
            if(maxh<np.bincount(tuph).argmax()):
                maxh=len(human)
                cv2.imwrite('human.jpg',img)
        if (tup2[1] == 1):
            tiger = tiger_cascade.detectMultiScale(gray, 1.3, 5)
            lt.append(tiger)
            tupt.append(len(tiger))
            tupt.pop(0)
            if (maxt < np.bincount(tupt).argmax()):
                maxt=len(tiger)
                cv2.imwrite('tiger.jpg', img)
        if(tup2[2]==1):
            rhino=rhino_cascade.detectMultiScale(gray,1.9,5)
            lt.append(rhino)
            tupr.append(len(rhino))
            tupr.pop(0)
            if (maxr < np.bincount(tupr).argmax()):
                maxr = len(rhino)
                cv2.imwrite('rhino.jpg', img)
        if(tup2[3]==1):
            bear=bear_cascade.detectMultiScale(gray,12,12)
            lt.append(bear)
            tupb.append(len(bear))
            tupb.pop(0)
            if (maxb< np.bincount(tupb).argmax()):
                maxb = len(bear)
                cv2.imwrite('bear.jpg', img)
        if(tup2[4]==1):
            lion=lion_cascade.detectMultiScale(gray,2,6)
            lt.append(lion)
            tupl.append(len(lion))
            tupl.pop(0)
            if (maxl < np.bincount(tupl).argmax()):
                maxl=len(lion)
                cv2.imwrite('lion.jpg', img)
        if(tup2[5]==1):
            cat=cat_cascade.detectMultiScale(gray,1.3,5)
            lt.append(cat)
            tupc.append(len(cat))
            tupc.pop(0)
            if (maxc < np.bincount(tupc).argmax()):
                maxc = len(cat)
                cv2.imwrite('cat.jpg', img)
        #Remove it after demonstaration
        '''for i in lt:
            for(x,y,w,h) in i:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                oi_gray = gray[y:y + h, x:x + w]
                oi_gray = gray[y:y + h, x:x + w]'''
        
        print "Max Humans==>"+str(maxh)
        print "Max Tigers==>"+str(maxt)
        print "Max Rhinos==>"+str(maxr)
        print "Max Bears==>"+str(maxb)
        print "Max Lions==>"+str(maxl)
        print "Max Cat==>"+str(maxc)
        print str(yu)
        tup=(human,tiger,rhino,bear,lion,cat)
        for  i in tup:
            for (x,y,w,h) in i:
                if(len(human)>0):
                   #font=cv2.FONT_HERSHEY_SIMPLEX
                   #cv2.putText(img, 'Human',(x-w,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)
                   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                   roi_gray = gray[y:y+h, x:x+w]
                if(len(rhino)>0):
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
                   roi_gray = gray[y:y+h, x:x+w]
                if(len(tiger)>0):
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                   roi_gray = gray[y:y+h, x:x+w]
                if(len(lion)>0):
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                   roi_gray = gray[y:y+h, x:x+w]
                if(len(bear)>0):
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                   roi_gray = gray[y:y+h, x:x+w]
                if(len(cat)>0):
                   cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
                   roi_gray = gray[y:y+h, x:x+w]
                #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #roi_gray = gray[y:y+h, x:x+w]
               #eyes = eye_cascade.detectMultiScale(roi_gray)
               # for (ex,ey,ew,eh) in eyes:
               #  cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    counter=0
    cap.release()
    cv2.destroyAllWindows()
    out.release()
    maxnum=[maxh,maxt,maxr,maxb,maxl,maxc]
    alert_func(maxnum,tup1,mail_status,sms_status)
#print(sendtoserver("Hi"))
    
    
while(True):
    z=readPIR()
    if(z=="0"):
        time.sleep(0.5)
    else:
        tcpmsg()
        cameraditection(alert_tcp, status_tcp,statuses_tcp[2],statuses_tcp[3])
        #sendsms("Hi How are you?")
        #sendemail(alert,"Tiger and Lion Detected!")
        '''smsmessage="ALERT! "
        smsmessage +=str(2) + " lion(s) \n"
        smsmessage += str(3) + " cats(s) \n"
        if(smsmessage!='ALERT! '):
            smsmessage+="detected."
            sendsms(smsmessage)'''
        
