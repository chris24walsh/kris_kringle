import smtplib

server = smtplib.SMTP('smtp.gmail.com', 25)
server.connect("smtp.gmail.com",465)
server.ehlo()
server.starttls()
server.ehlo()
server.login("chris24walsh@gmail.com", "3KESVWxG4bi7")

#send the mail
msg = "Hello!"
server.sendmail("chris24walsh@gmail.com", "chris24walsh@gmail.com", msg)
server.quit()
