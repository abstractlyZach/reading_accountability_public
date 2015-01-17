# check zachary.lee.email.bot 's email and update the spreadsheet based on responses 
# runs every 5 minutes between 3pm and 4am 
*/5 0-3,15-23 * * * python Documents/workspace/manageemail/emailchecker.py 
 
 
# send out emails daily 
0 15 * * 1-6 python Documents/workspace/manageemail/emailsender.py  
 
 
# fill in the blanks for people who did not respond 
0 4 * * 0,2-6 python Documents/workspace/manageemail/fillinblanks.py 
 
 
# increase the chapter number for the week 
0 8 * * 4 python Documents/workspace/manageemail/weeklychapter.py 
