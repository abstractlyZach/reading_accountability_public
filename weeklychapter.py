import gspread # https://github.com/burnash/gspread
import email_info

sg_spreadsheet = gspread.login(email_info.get_login(), email_info.get_password())

reading_log = sg_spreadsheet.open("AACF Freshman Small Group Reading").worksheets()[0]
chapter_cell_str = "A12"

reading_log.update_acell(chapter_cell_str, int(reading_log.acell(chapter_cell_str).value) + 1)
