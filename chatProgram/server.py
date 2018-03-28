import socket
import sys
import threading
import os

HOST = input("Enter local IP: ")
PORT = int(input("Enter port: "))
PASSWORD = input("Server password: ")
CLIENTS = []
BLACKLIST = []
BUFFER_SIZE = 4096

def send_all(msg, dont_send):
	for client in CLIENTS:
		if client == dont_send:
			pass
		else:
			client.send(msg)

def handle_client(client, addr, bufsiz):
	client_name = client.recv(bufsiz).decode("utf8")
	client_password = client.recv(bufsiz).decode("utf8")
	if client_password != PASSWORD:
		send_all(bytes("{} got the password incorrect he/she is not to be trusted".format(client_name), "utf8"), client)
		BLACKLIST.append(addr)
		client.close()
		sys.exit()
	send_all(bytes("{} joined us".format(client_name), "utf8"), client)
	CLIENTS.append(client)

	while True:
		client_msg = client.recv(bufsiz)
		if client_msg.decode("utf8") == "exit":
			client.close()
			sys.exit()
		print(client_msg.decode("utf8"))
		send_all(client_msg, client)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST, PORT))

try:
	os.system("cls")
except:
	os.system("clear")

print("Server started...")
print("Server IP: {}".format(HOST))
print("Server Port: {}".format(PORT))
print("Server Password: {}".format(PASSWORD))

ss.listen(5)

while True:
	client, client_addr = ss.accept()
	if client_addr in BLACKLIST:
		client.close()
	else:
		print("{} connected!".format(client_addr))
		threading.Thread(target=handle_client, args=(client, client_addr, BUFFER_SIZE, )).start()
