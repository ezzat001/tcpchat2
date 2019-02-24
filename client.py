
import socket,select,sys,time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.3'
host = raw_input("Enter your host ip : ")
if len(host) < 8:
    host= "192.168."+host
name = raw_input("Enter your name : ")
def ipg(): 
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
   try: 
 
      s.connect(('10.255.255.255', 1)) 
      IP = s.getsockname()[0] 
   except: 
      IP = '127.0.0.1' 
   finally: s.close() 
   return IP
ip = str(ipg())
try:
    server.connect((host,4444))
    server.send(("[+] %s is in as %s"%(ip,name)).encode())
except Exception as e:
    print("Invaild Data")
    exit()
    

def send():
    server.send(("<%s> %s"%(name,message)).encode())
while True: 

	sockets_list = [sys.stdin, server] 

	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print(message.decode())
		else: 
			message = sys.stdin.readline() 
			send()

			#sys.stdout.write(message)
			sys.stdout.flush() 
server.close() 
