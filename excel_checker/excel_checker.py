from xlrd import open_workbook

rb = open_workbook('table_1.xlsx')
sheet = rb.sheet_by_index(0)
value = '2607405'
for ii in range(sheet.nrows):
    data = sheet.cell_value(ii, 2)
    print(data)