# reading_accountability_public
Designed to automate public accountability for AACF UCI Freshman small group. http://goo.gl/zjL0GN

============

Backstory:
-------------
Each of us in our group agreed that we wanted to create good habits and that one of those habits we wanted to develop was daily reading. However, at each weekly meeting, we would discuss whether or not we had been able to keep up with reading a mere 2 pages per day (based on page numbers, so each face of a physical page counts as a "page of reading"), and an overwhelming amount of us shared that we didn't keep up with the reading, myself included most of the time. Every week that I forgot to uphold my commitment to reading daily, I would walk away slightly embarassed and ashamed that I let myself and let the rest of the guys down. And then I would quickly get over it and make the same mistakes again. It wasn't a problem of time; daily readings took less than 5 minutes per day. It wasn't a problem of logic; all of us were convinced that this endeavor was worth our time and effort. From what I could tell, one of the true problems that we were dealing with was that the level of accountability didn't match the task we set before ourselves. 

We needed a system that would:

0. record who read each day so that all group members could see
0. minimize effort on the group members' side so that there would be the fewest reasons possible to feel 
      (consciously or unconsciously) that the reading and its associated tasks were a chore
0. not require tremendous upkeep. The system should be autonomous and low-maintenence. Whoever has to take care     of it should only have to deal with the occasional minor bugs.
 
It was time to stop only "trying harder"; it was time to leverage psychology and programming to achieve our goals.



These are the features I used to execute our goals (and some more to boot!):

* daily emails
* automated spreadsheet updating
    - social comparison theory
    - Hawthorne Effect
    - ability to see trends and use that information to understand ourselves better
* statistics page
    - fun metrics (leaderboard, streak counters)
    - "What gets measured gets managed" --Peter Drucker
    - group statistics: can compare each of us to see how me measure up to the overall group 
* goals and rewards
    - reminds us that others are watching and supporting us
    - gives our supporters a method of involving themselves with our project
    - gives us more excuses to have fun with this project and get to know each other as well as our supporters better
    




-------------
Technical details:
-------------
I wrote another script called email_info.py with functions that return my login credentials (get_login() and 
get_password()) and a function that returns a dictionary mapping the names to the emails of all of the people on the
mailing list (get_email_dict()).

I'm using crontab to schedule my computer to run the scripts at specific intervals. You can see my crontab
file, which is named crontab_file.txt in this repository. 
