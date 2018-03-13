import datetime
import xlsxwriter
from config import excel_files


def write_to_excel_file(data):
    now = datetime.datetime.now()
    excel_filename = now.strftime("{}/%Y-%m-%d_%H:%M.xlsx".format(excel_files))
    workbook = xlsxwriter.Workbook(excel_filename)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Current Name")
    worksheet.write(0, 1, "Name in Database")
    row, col = 1, 0
    for current, orig in data:
        worksheet.write(row, col, current)
        worksheet.write(row, col + 1, orig)
        row += 1
    workbook.close()