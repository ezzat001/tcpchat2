#writing last two numbers .. from the host ip instead of 192.168.x.x
#kick , mute ,clear commands
#accounts
import socket 
import select 
import sys,os
from thread import *
host = socket.gethostname()

print("Welcome to Ezzat's Chat Server Side\n")
def ge(): 
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
   try: 
 
      s.connect(('10.255.255.255', 1)) 
      IP = s.getsockname()[0] 
   except: 
      IP = '127.0.0.1' 
   finally: s.close() 
   return IP





server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

	
ipaddr = ge()
IP_address = ipaddr



server.bind((IP_address, 4444)) 

server.listen(100) 
chatname = raw_input("Enter the Chat room name : ")
print("[+] Server is up")
print("Server Name : %s\nRoom Name : %s\nHost : %s"%(host,chatname,ipaddr))

list_of_clients = [] 
muted = []
def clientthread(conn, addr): 

	conn.send("Welcome to "+chatname+" chat!".encode()) 

	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 
					if "clearnow" in message.decode():
						for i in range(10000):
							broadcast("Counting to 10000 -> "+str(i),conn)
							conn.send("Counting to 10000 -> "+str(i))
					elif "clear1000" in message.decode():
						for i in range(1000):
							broadcast("Counting to 1000 -> "+str(i),conn)
							conn.send("Counting to 1000 -> "+str(i))
					elif "clear5000" in message.decode():
						for i in range(5000):
							broadcast("Counting to 5000 -> "+str(i),conn)
							conn.send("Counting to 5000 -> "+str(i))
					elif "massclear" in message.decode():
						for i in range(50000):
							broadcast("Counting to 50000 -> "+str(i),conn)
							conn.send("Counting to 50000 -> "+str(i))
					elif "clearallshit" in message.decode():
						for i in range(100000):
							broadcast("Counting to 100000 -> "+str(i),conn)
							conn.send("Counting to 100000 -> "+str(i))
					elif "mute" in message.decode():
						msgd = message.decode()
						mutedname = msgd.find("mute")
						mutedname2 = (msgd[mutedname+4:]).replace(" ","")
						muted.append(mutedname2)
					else:
						print(message.decode())

						# Calls broadcast function to send message to all 
						#message_to_send = "<%s> %s"%("SERVER",message.encode())
						broadcast(message, conn) 
						
				
				else: 
					
					remove(conn) 

			except: 
				continue

def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message.encode()) 
			except: 
				clients.close() 

				remove(clients) 
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True: 

	conn, addr = server.accept() 
	list_of_clients.append(conn) 

	#print(addr[0] + " is on")

 	

	start_new_thread(clientthread,(conn,addr))

conn.close() 
server.close() 
