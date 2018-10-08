import time
from datetime import datetime as dt
host_path = '/etc/hosts'
redirect = '127.0.0.1 '
sites_to_block= [' https://www.facebook.com/',' facebok.com',' www.facebook.com',' gmail.com',' www.gmail.com']
print(dt.now())
while True:
 if dt(dt.now().year, dt.now().month, dt.now().day,10)< dt.now()< dt(dt.now().year, dt.now().month, dt.now().day,23):
  print("working hours! now social media allowed")
  with open(host_path,'r+') as file:
    content = file.read()
    print(content )
    for site in sites_to_block:
      print(site)
      if site in content:
       pass
      else:
       file.write(redirect +''+site+'\n')
 else:
   with open(host_path, 'r+') as file:
    content = file.readlines()
    file.seek(0)
    for line in content:
     if not any (site in line for site in sites_to_block):
        file.write(line)
    file.truncate()
   print("time to play! around the web that bore me")
 time.sleep(2)
