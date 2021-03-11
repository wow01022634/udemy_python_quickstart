import openpyxl
#change path to your local directory
path = 'c:/Users/Andrew A/Desktop/python_demo/7_Working_with_Excel/'
book = openpyxl.Workbook()
sheet = book.create_sheet("latin")
rows = [
    [77,88,99],
    [74,83,93],
    [77,85,59]
]
for row in rows:
    sheet.append(row)

book.save(path + "new2.xlsx")
 