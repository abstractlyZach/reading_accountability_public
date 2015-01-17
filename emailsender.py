import sendemail
import email_info

email_list = email_info.get_email_dict().keys()
              
#email_list = ["zalee@uci.edu"] #sends emails to myself for testing purposes

original_text = ( \
"""Have you taken care of today's reading for AACF Freshman Small Group?
Respond with 'Y' or 'y' for 'yes' and anything else for 'no'.
See the current spreadsheet at http://goo.gl/zjL0GN""")

sendemail.run(original_text, email_list)
