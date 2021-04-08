import smtplib
import time
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("brianyin09@gmail.com", "Brian!123")
 
msg = "Huaqi Yin is Awesome lazy!"

if __name__ == '__main__':
    while True:
	server.sendmail("winston@elobal.com", "yinleew@gmail.com", msg)
	server.quit()
        time.sleep(10)

