import xlsxwriter
workbook=xlsxwriter.Workbook("Excell.xlsx")
sheet=workbook.add_worksheet()
r=0
c=0

data=( ['AD',22],['Akkie',232],['money',786] )

for i,j in (data):
    sheet.write(r,c,i)
    sheet.write(r,c+1,j)
    r+=1

workbook.close()