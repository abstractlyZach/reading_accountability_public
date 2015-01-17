import smtplib
import time, datetime
import email_info
    
    
def run(original_text, toaddrs_list):
    from email.mime.text import MIMEText
     
    username = email_info.get_login()
    password = email_info.get_password()
    
    now = datetime.datetime.now()
    print('[{}-{}-{} {}:{}:{}] sending emails...'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))

    fromaddr = 'zachary.lee.email.bot@gmail.com' # this line just has to have something. the email address here can be bogus if you 
      
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)

    # adding extra text to the end of every message. just reminding them that
    # a bot is sending out these emails.
    original_text += (
"""\n-----------------------------\n\nThis is an automated message from Zach\'s email bot. 
If you wish to contact Zach directly, email him at Zach3Lee@gmail.com. 
Zach does not read emails that are sent to this bot."""
    )
    
    for toaddrs in toaddrs_list:
        
        msg = MIMEText(original_text)
         
        msg['Subject'] = "AACF Freshman Small Group Reading"
        msg['From'] = fromaddr
        msg["To"] = toaddrs
    
        # server.send_message(msg) #This is for Python 3

        server.sendmail(msg['From'], [msg['To']], msg.as_string()) #this is for Python 2.7
        
    server.quit()
    
    now = datetime.datetime.now()
    print('[{}-{}-{} {}:{}:{}] emails have been sent.'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
    
if __name__ == "__main__":
    print("you ran the wrong file, dummy")
