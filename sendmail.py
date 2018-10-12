import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("anjankumar04419@gmail.com", "9435404419") 
  
# message to be sent 
message = "hello dude"
  
# sending the mail 
s.sendmail("anjankumar04419@gmail.com", "bhargavsp11@gmail.com", message) 
  
# terminating the session 
s.quit() 

