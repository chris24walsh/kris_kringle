#!/usr/bin/python

import random
import smtplib

#Make list of names
names = [
  "JP:listoweljp@yahoo.com",
  "Fidelma:fidelman05@gmail.com",
  "Steven:steven.walsh39@gmail.com",
  "Selwan:s.tangwalsh@gmail.com",
  "Philip:philipewalsh@icloud.com",
  "Katie:katiesarahfrench@gmail.com",
  "Chris:chris24walsh@gmail.com",
  "Iryna:iryna.kizym@gmail.com",
  "Abigail:Abigail.Walsh12@gmail.com",
  "Lisa:lwalsh8@tcd.ie",
  "Young:soonyo@tcd.ie"
]

#run scramble in loop, until it satisfies constraints
constraints_met = False
trying = 0
while constraints_met != True:
  trying += 1
  print('Try ' + str(trying)) 
  #Scramble list
  scramble = list(names)
  random.shuffle(scramble)
  
  #turn each element into sub-array, with each name paired with the following one
  tmp = scramble[0]
  for i in range(0, ( len(scramble) - 1 )):
    scramble[i] = [ scramble[i], scramble[i+1] ]
  scramble[ len(scramble) - 1 ] = [ scramble[ len(scramble) - 1 ], tmp ]
  
  #check constraints
  constraints_met = True
  for i in range(len(scramble)):
    if any( [ scramble[i] == ['JP:listoweljp@yahoo.com', 'Fidelma:fidelman05@gmail.com'], scramble[i] == ['Steven:steven.walsh39@gmail.com', 'Selwan:s.tangwalsh@gmail.com'], scramble[i] == ['Philip:philipewalsh@icloud.com', 'Katie:katiesarahfrench@gmail.com'], scramble[i] == ['Chris:chris24walsh@gmail.com', 'Iryna:iryna.kizym@gmail.com'], scramble[i] == ['Young:soonyo@tcd.ie', 'Lisa:lwalsh8@tcd.ie'], scramble[i] == ['Fidelma:fidelman05@gmail.com', 'JP:listoweljp@yahoo.com'], scramble[i] == ['Selwan:s.tangwalsh@gmail.com', 'Steven:steven.walsh39@gmail.com'], scramble[i] == ['Katie:katiesarahfrench@gmail.com', 'Philip:philipewalsh@icloud.com'], scramble[i] == ['Iryna:iryna.kizym@gmail.com', 'Chris:chris24walsh@gmail.com'], scramble[i] == ['Lisa:lwalsh8@tcd.ie', 'Young:soonyo@tcd.ie'], scramble[i] == ['JP:listoweljp@yahoo.com', 'Selwan:s.tangwalsh@gmail.com'], scramble[i] == ['JP:listoweljp@yahoo.com', 'Katie:katiesarahfrench@gmail.com'], scramble[i] == ['JP:listoweljp@yahoo.com', 'Iryna:iryna.kizym@gmail.com'], scramble[i] == ['JP:listoweljp@yahoo.com', 'Young:soonyo@tcd.ie'] ] ):
      print("Error")
      print(scramble[i])
      constraints_met = False
  if ( constraints_met == True ):
    print("Success")
    break
  
#print scramble_names
print scramble

#setup mail server
server = smtplib.SMTP('smtp.gmail.com',587)

#login to mail server
#server.login(MAIL_USERNAME, MAIL_PASSWORD)
server.login("chris24walsh@gmail.com", "3KESVWxG4bi7")
server.connect("smtp.gmail.com",465)
server.ehlo()
server.starttls()
server.ehlo()

#send the mail
msg = "\nHello!"
server.sendmail("chris24walsh@gmail.com", "chris24walsh@gmail.com", msg)

