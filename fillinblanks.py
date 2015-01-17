import gspread # https://github.com/burnash/gspread
import processemail
import datetime
import email_info

EMAIL_ACCOUNT = email_info.get_login()
EMAIL_PASS = email_info.get_password()
spreadsheet_name = "AACF Freshman Small Group Reading"

processemail.write_to_log("[{}] filling in blanks.".format(processemail.current_timestamp()))

gc = gspread.login(EMAIL_ACCOUNT, EMAIL_PASS)
worksheet = gc.open(spreadsheet_name).sheet1
stats = gc.open(spreadsheet_name).worksheets()[1]

today = datetime.datetime.now() - datetime.timedelta(days = 1)

worksheet_dates = worksheet.row_values(1)
today_column = worksheet_dates.index(str(today.date())) + 1

responses = worksheet.col_values(today_column)
for person_row in range(2, 10):
		if responses[person_row - 1] == None:
			name = worksheet.cell(person_row, 1).value
			processemail.add_fail_entry(name, spreadsheet_name)
			processemail.end_streak(name, spreadsheet_name)
			worksheet.update_cell(person_row, today_column, "N")

			processemail.write_to_log("     Person in row #{} did not respond today.\n".format(person_row + 1))
			stats.update_acell("H3", int(stats.acell("H3").value) + 1)

stats.update_acell("G3", int(stats.acell("G3").value) + 1)
