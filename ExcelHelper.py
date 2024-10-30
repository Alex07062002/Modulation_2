import openpyxl


def open_and_write_to_excel(array, name_column, file)->None:
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    number_column = ord(name_column.lower()) - 96
    for i in range (len(array)):
        sheet.cell(row=i+2,column= number_column).value = array[i]
    workbook.save(file)
    return None