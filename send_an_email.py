import smtplib
import time
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("brianyin09@gmail.com", "******")
 
msg = "Ms. Yin is Awesome lazy!"

if __name__ == '__main__':
    while True:
	server.sendmail("winston@winston.com", "winston@usa.com", msg)
	server.quit()
        time.sleep(10)

