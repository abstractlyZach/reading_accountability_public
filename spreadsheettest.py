import gspread

gc = gspread.login("zachary.lee.email.bot", "email bot of zachary lee")

worksheet = gc.open("The ULTIMATE Spreadsheet").sheet1

worksheet.update_cell(1, 2, "HOWDY THERE")
    
better_cell_list = worksheet.row_values(1)
for cell in better_cell_list:
    print(cell)
    
print(better_cell_list)

print("done!")