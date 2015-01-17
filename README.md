# reading_accountability_public
Designed to automate public accountability for AACF UCI Freshman small group. http://goo.gl/zjL0GN


I know my naming conventions are all over the place. I didn't expect this project to be 
as big as it ended up being hahahaha
It started as a small project to hack something together and put my Raspberry Pi to good use,
and now I've sunk around 25 hours into this project.

I wrote another script called email_info.py that holds my login credentials with get_login() and 
get_password() as well as a dictionary holding the emails and names of all of the people on the
mailing list. 

I'm using crontab to schedule my computer to run the scripts at specific intervals. You can see my crontab
file, which is named crontab_file.txt in this repository. 

If you'd like to use my code, feel free to! Just contact me and you'll need to create your own crontab file
as well as an email_info.py file.
