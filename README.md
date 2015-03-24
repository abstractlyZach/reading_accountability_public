# reading_accountability_public
Designed to automate public accountability for AACF UCI Freshman small group. 

See the spreadsheet here!

http://goo.gl/zjL0GN

============

Backstory:
-------------
Each of us in our group agreed that we wanted to create good habits and that one of those habits we wanted to develop was daily reading. However, at each weekly meeting, we would discuss whether or not we had been able to keep up with reading a mere 2 pages per day (based on page numbers, so each face of a physical page counts as a "page of reading"), and an overwhelming amount of us shared that we didn't keep up with the reading, myself included most of the time. Every week that I forgot to uphold my commitment to reading daily, I would walk away slightly embarassed and ashamed that I let myself and let the rest of the guys down. And then I would quickly get over it and make the same mistakes again. It wasn't a problem of time; daily readings took less than 5 minutes per day. It wasn't a problem of logic; all of us were convinced that this endeavor was worth our time and effort. From what I could tell, one of the true problems that we were dealing with was that the level of accountability didn't match the task we set before ourselves. 

We needed a system that would:

0. Record who read each day so that all group members could see.
0. Minimize effort on the group members' side so that there would be the fewest reasons possible to feel 
      (consciously or unconsciously) that the reading and its associated tasks were a chore.
0. Not require tremendous upkeep. The system should be autonomous and low-maintenence. Whoever has to take care     of it should only have to deal with the occasional minor bugs.
 
It was time to stop only "trying harder"; it was time to leverage programming skills and psychology to achieve our goals.



Features
---------
* daily emails
    - the scripts log into my email account and send out emails every day, prompting group members to respond if they completed their reading for the day.
* automated spreadsheet updating      
    - the scripts parse through my email inbox and update the spreadsheet based on responses from group members
    - social comparison theory (http://en.wikipedia.org/wiki/Social_comparison_theory): 
    
            - "Joe missed 2 readings this week and I only missed 1. Good for me!"
            
            - "Bob had a perfect week. He's nothing special; if he can do it, so can I!"
    - Hawthorne Effect AKA Observer Effect (http://en.wikipedia.org/wiki/Hawthorne_effect): People perform better when they perceive that others are observing them.
    - ability to see trends and use that information to understand ourselves better
* statistics page
    - fun metrics (leaderboard, streak counters). Who doesn't like being king of the hill? (Comes complete with bragging rights.)
    - "What gets measured gets managed" --Peter Drucker
    - group statistics: We can compare each of us to see how me measure up to the overall group.
* goals and rewards
    - reminds us that others are watching and supporting us
    - gives our supporters a method of involving themselves with our project
    - gives us more excuses to have fun with this project and get to know each other as well as our supporters
    


Technical details:
-------------
emailinfo.py:
Contains functions that return my login credentials (get_login() and get_password()) and a function that returns a dictionary mapping the names to the emails of all of the people on the mailing list (get_email_dict()). This is not included in my Github repository since it contains my credentials and other people's email addresses.

crontab_file.txt:
I'm using crontab to schedule my computer to run the scripts at specific intervals. It's a utility that comes with most Unix systems that you can set up to schedule your computer to automatically run programs at specific times.

* emailsender.py:
      - Executes email sending by calling functions in sendemail.py. Logs into my email account and sends out emails to everyone on the mailing list (found in emailinfo.py)

* sendemail.py:
      - Contains the functions to be called in emailsender.py for sending emails. Uses smtplib to take care of logging in and sending emails. Writes errors to the emailcheckerlog.txt.

* emailchecker.py:
      - Executes email checking by calling functions in process. Parses through my email inbox and updates the spreadsheet based on the responses, and then archives all processed emails. 

* processemail.py:
      - Contains the functions to be called in emailchecker.py for processing emails. Uses gspread (https://github.com/burnash/gspread) to update the spreadsheet and imap4 to process emails. Writes errors to the emailcheckerlog.txt.

* fillinblanks.py:
      - Runs every morning at 4AM (except Sunday morning) to fill in the blanks in the spreadsheet for the people who didn't respond. Uses gspread to update the spreadsheet.

* weeklychapter.py:
      - Updates the "Current Chapter" cell on the spreadsheet every Thursday. Uses gspread to update the spreadsheet.


Results (as of 2015-03-23)
-------------

We weren't logging data before this project, but based on verbal responses and my memory (of those verbal responses), our group was reading at a 37.5% rate: every time our group of 8 people met, there were usually 3 who had completed all of their readings for the week and 5 who hadn't. After logging 7 days with the system, the group read at 79.13% rate, a huge improvement! Dazzling success! 

Now, there are some differences to note. With the 37.5% statistic, we were polling the group members weekly. With the 79.13% statistic, we were polling the group members daily. There were cases where people would miss a reading with the old system and then they would give up on the entire week's readings. Also, if someone read 5/6 days with the old system, they would contribute a 0/1 to the group's statistic. However, with the new system, if someone read 5/6 days, they would contribute a 5/6 to the group, making our new statistics more accurate than the old statistics. Because of the reasons above, the 37.5% statistic is surely lower than reality. One of the great things that I've noticed is that the new system eliminated the cases where people would give up halfway through the week because now they had a new chance the next day, rather than having to wait for the week to end to have that second chance!

There was a day where our group (who was averaging 85% at the time) read at a rate of 37.5% on a specific day. It was a major slump in our scores! Many reading streaks died that day :( . It was pretty discouraging for us. However, because of our newer, finer-grained system, we were able to pull up the metrics and try to understand what caused such widespread failure. We did a lot of introspection and I'm sure that many of us were gained a bit of insight on our behaviors through examining such an interesting trend. I know I did! The general consensus was that most of us missed that day because it was a holiday and it was right before midterms, so we had various reasons for missing reading that day (forgot, stressed with schoolwork, refused to check email at all because it was a holiday, etc.). Because of the data we were collecting, we were able to pinpoint a common failure point. Because of the data we were collecting, we equipped ourselves with the tools necessary to understand ourselves a bit better and we opened up the door to alter our behavior. We wouldn't have been able to do this otherwise!
