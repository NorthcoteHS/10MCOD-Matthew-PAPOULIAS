import socket
import sys
import os
import threading

notify = True

try:
	from win10toast import ToastNotifier
except ModuleNotFoundError:
	print("[!] win10toast module not found")
	install = input("Would you like it to be installed now (y/n): ")
	if install == "y":
		os.system("pip install win10toast")
	else:
        print("Notifications will not work!")
        notify = False

def recieve(s, bufsiz):
	while True:
		msg = s.recv(bufsiz).decode("utf8")
		print(msg)
        if notify:
            notifier.show_toast("Chat App", msg, duration=3, threaded=True)

def send(s):
	while True:
		msg = input()
		if msg == "exit":
			s.send(bytes(msg, "utf8"))
			s.close()
			sys.exit()
		msg = PREFIX + msg
		s.send(bytes(msg, "utf8"))

print("Welcome to Simple Chat Program")
ip = input("Server IP: ")
port = input("Server port: ")
notifier = ToastNotifier()
SERVER_IP = ip
SERVER_PORT = int(port)
ADDR = (SERVER_IP, SERVER_PORT)
BUFFER_SIZE = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(ADDR)
name = input("Enter name: ")
password = input("Enter password: ")
PREFIX = name + ": "
s.send(bytes(name, "utf8"))
s.send(bytes(password, "utf8"))

threading.Thread(target=recieve, args=(s, BUFFER_SIZE, )).start()
threading.Thread(target=send, args=(s, )).start()
while 1:
	pass
