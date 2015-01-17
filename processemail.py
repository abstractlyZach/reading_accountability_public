import sys
import imaplib
import email, email.utils
import datetime, time
import gspread # https://github.com/burnash/gspread
import email_info
 
EMAIL_ACCOUNT = email_info.get_login()
EMAIL_PASS = email_info.get_password()
EMAIL_FOLDER = "PendingRequests"     

gc = gspread.login(EMAIL_ACCOUNT, EMAIL_PASS)


#make sure each of the email addresses are all lowercase
email_dict = email_info.get_email_dict()
 
M = imaplib.IMAP4_SSL('imap.gmail.com')


def process_mailbox(M, spreadsheet_name):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """
     
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        write_to_log("No messages found!\n")
        return
     
    email_counter = 0
    for num in data[0].split():
        rv, new_data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            write_to_log("ERROR getting message" + str(num) + "\n")
            return
        msg = email.message_from_string(new_data[0][1]) #change to message_from_bytes for Python3
        if msg["From"] != "zachary.lee.email.bot@gmail.com":
            email_counter += 1
          
    write_to_log("[{}] Emails to process: {}\n".format(current_timestamp(), email_counter))
         
    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        
        msg = email.message_from_string(data[0][1]) #change to message_from_bytes for Python3
        
        if msg["From"] == "zachary.lee.email.bot@gmail.com":
            continue
        
        if msg["From"].split()[-1] in email_dict:            
            write_to_log("[{}] Processing email from {}\n".format(current_timestamp(), email_dict[msg["From"].split()[-1]]))
            
            msg_date = email.utils.parsedate(msg["Date"])
    
            if msg.is_multipart():
                # for future debugging. These print statements helped me so much.
                # print("it's multipart.")
                # print(msg.get_payload(0).as_string().splitlines())
                if msg.get_payload(0).as_string().splitlines()[2].upper() == "Y":
                    add_entry_to_spreadsheet(email_dict[msg["From"].split()[-1]], True, spreadsheet_name)
                elif msg.get_payload(0).as_string().splitlines()[2].upper() == "" and msg.get_payload(0).as_string().splitlines()[3].upper() == "Y":
                    add_entry_to_spreadsheet(email_dict[msg["From"].split()[-1]], True, spreadsheet_name)
                else:
                    add_entry_to_spreadsheet(email_dict[msg["From"].split()[-1]], False, spreadsheet_name)
            else:
                # same as above.
                # print("it's not multipart.")
                # print(msg.get_payload().splitlines())
                if msg.get_payload().splitlines()[0].upper() == "Y":
                    add_entry_to_spreadsheet(email_dict[msg["From"].split()[-1]], True, spreadsheet_name)
                elif msg.get_payload().splitlines()[2].upper() == "" and msg.get_payload().splitlines()[3].upper() == "Y":
                    add_entry_to_spreadsheet(email_dict[msg["From"].split()[-1]], True, spreadsheet_name)
                else:
                    add_entry_to_spreadsheet(email_dict[msg["From"].split()[-1]], False, spreadsheet_name)
        else:
            write_to_log("[{}] Email from {}. Discarding...\n".format(current_timestamp(), msg["From"].split()[-1]))
    
          
    typ, data = M.search(None, 'ALL')
    for num in data[0].split():
        M.store(num, '+FLAGS', '\\Deleted')
    M.expunge()


def add_entry_to_spreadsheet(name, read, spreadsheet_name):
    today = datetime.datetime.now() - datetime.timedelta(hours = 4)
    
    write_to_log("[{}] adding entry: {}\n".format(current_timestamp(), name))

    if read:
        write_to_log("  {} has read today.\n".format(name))
    else:
        write_to_log("  {} did not read today.\n".format(name))

    worksheet = gc.open(spreadsheet_name).worksheets()[0]
    stats = gc.open(spreadsheet_name).worksheets()[1]
    
    worksheet_dates = worksheet.row_values(1)
    if (str(today.date()) not in worksheet_dates):
        worksheet.update_cell(1, len(worksheet_dates) + 1, "'" + str(today.date()))
        target_column = len(worksheet_dates) + 1
    else:
        target_column = worksheet_dates.index(str(today.date())) + 1
            
    worksheet_names = worksheet.col_values(1)
    if name not in worksheet_names:
        worksheet.update_cell(len(worksheet_names) + 1, 1, name)
        target_row = len(worksheet_names) + 1
    else:
        target_row = worksheet_names.index(name) + 1
            
    if read:
        add_success_entry(name, spreadsheet_name)
        continue_streak(name, spreadsheet_name)
        worksheet.update_cell(target_row, target_column, "Y")
    else:
        add_fail_entry(name, spreadsheet_name)
        end_streak(name, spreadsheet_name)
        worksheet.update_cell(target_row, target_column, "N")

    stats.update_acell("H3", int(stats.acell("H3").value) + 1)


def add_success_entry(name, spreadsheet_name):
    stats = gc.open(spreadsheet_name).worksheets()[1]

    user = stats.find(name)

    stats.update_cell(user.row, 2, int(stats.cell(user.row, 2).value) + 1)


def add_fail_entry(name, spreadsheet_name):
    stats = gc.open(spreadsheet_name).worksheets()[1]

    user = stats.find(name)

    stats.update_cell(user.row, 3, int(stats.cell(user.row, 3).value) + 1)



def continue_streak(name, spreadsheet_name):
    stats = gc.open(spreadsheet_name).worksheets()[1]

    user = stats.find(name)

    stats.update_cell(user.row, 5, int(stats.cell(user.row, 5).value) + 1)


def end_streak(name, spreadsheet_name):
    stats = gc.open(spreadsheet_name).worksheets()[1]

    user = stats.find(name)

    stats.update_cell(user.row, 5, 0)   
    

def current_timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
def run(spreadsheet_name):     
    try:
        rv, data = M.login(EMAIL_ACCOUNT, EMAIL_PASS) #getpass.getpass())
    except imaplib.IMAP4.error:
        write_to_log("LOGIN FAILED!!! \n")
        sys.exit(1)
     
    write_to_log("[{}]".format(current_timestamp()) + str(rv) + str(data) + "\n")
     
    rv, mailboxes = M.list()
    if rv == 'OK':
    #     write_to_log("Mailboxes:")
    #     write_to_log(mailboxes)
        pass
     
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        write_to_log("[{}] Processing mailbox...\n".format(current_timestamp()))
        process_mailbox(M, spreadsheet_name)
        M.close()
    else:
        write_to_log("ERROR: Unable to open mailbox.\n", rv)
        
    M.logout()
    
    write_to_log("[{}] Mailbox successfully processed.\n".format(current_timestamp()))
    
    write_to_log("\n---------\n\n")

    
def write_to_log(text):
    file = open("emailcheckerlog.txt", "a")
    file.write(text)
    file.close()
    

if __name__ == "__main__":
    print("you're running the wrong file, dummy.")
