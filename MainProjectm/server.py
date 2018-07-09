import socket
#import main
import time
global connec

def connec():
        BUFFER_SIZE = 1000
        s = socket.socket()         # Create a socket object
        #host = '192.168.43.253' # Get local machine name
        host = '192.168.43.253'
        port = 8001          # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port
        data=""
        s.listen(5)                 # Now wait for client connection.
        #IF DATA==QUIT server will do down
        while data!='QUIT':
                c = s.accept()[0]
                data=c.recv(BUFFER_SIZE)
                
                if data == '':
                         time.sleep(1)
                else:
                            #print data
                            if(len(data)==16):
                                spli(data)
                            c.send("Done")
        c.close()
        s.close()
        
           
        
###########################################################
######### WE ARE WRITING THE OUTPUT TO THE TEXT FILE ######
###########################################################
def spli(d):
       # p=main.Master()
       #Openning File or Creating
        f = open("tcpmsg.txt",'w')
        f.write(d)
        f.close()

connec()
                    
                
        

        
        
       

        
        
     
        
