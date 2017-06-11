import webbrowser
import time

cnt = 3
print("This program started at " + time.ctime())
while cnt:
	time.sleep(10)
	webbrowser.open('https://www.google.com/')
	cnt -= 1