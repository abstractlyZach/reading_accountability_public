# reading_accountability_public
Designed to automate public accountability for AACF UCI Freshman small group. http://goo.gl/zjL0GN

I wrote another script called email_info.py with functions that return my login credentials (get_login() and 
get_password()) and a function that returns a dictionary mapping the names to the emails of all of the people on the
mailing list (get_email_dict()).

I'm using crontab to schedule my computer to run the scripts at specific intervals. You can see my crontab
file, which is named crontab_file.txt in this repository. 
