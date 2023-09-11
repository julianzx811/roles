import openpyxl
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if "GET" == request.method:
        return render(request, "Archivos/index.html", {})
    else:
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        print(worksheet)

        # getting active sheet
        active_sheet = wb.active
        print(active_sheet)

        # reading a cell
        print(worksheet["C1"].value)

        excel_data = []
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows(min_row=12, max_row=59, max_col=8):
            row_data = []
            for cell in row:
                if(str(cell.value)!='None'):
                    row_data.append(str(cell.value))
                    print(cell.value)
            if len(row_data) > 1:
                excel_data.append(row_data)
        print(excel_data)

        return render(request, "Archivos/index.html", {"excel_data": excel_data})
