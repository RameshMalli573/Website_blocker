import time
from datetime import datetime as dt
host_path = "C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("working hours!!!")
        with open("hosts",'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                     with open("hosts",'r+') as file:
                         content = file.read()
                         file.write(redirect+" "+website+"\n")
time.sleep(5)
    
