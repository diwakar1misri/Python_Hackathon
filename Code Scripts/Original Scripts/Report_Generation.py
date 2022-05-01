import os
import xlsxwriter
def Report_Generation(file_data_1,file_data_2):
    workbook1_row = 1
    workbook2_row = 1
    path = os.path.abspath("").replace("Code Scripts", "")
    report = xlsxwriter.Workbook(path + "Report_Generated_Summary.xlsx")
    workbook1 = report.add_worksheet("Matched")
    workbook2 = report.add_worksheet("Unmatched")
    workbook1.write(0, 0, "Key")
    workbook1.write(0, 1, "Data")
    workbook2.write(0, 0, "Key")
    workbook2.write(0, 1, "Data")
    workbook2.write(0, 2, "Matching rows")
    workbook2.write(0, 3, "File 1 has more rows than by File 2")
    workbook2.write(0, 4, "File 2 has more rows than by File 1")
    for itr in file_data_1:
        if itr[2]==itr[3]:
            print(f"Data: {itr[0]} with key {itr[1]} -> Match in Both the Files")
            workbook1.write(workbook1_row,0,itr[1])
            workbook1.write(workbook1_row,1,str(itr[0]))
            workbook1_row=workbook1_row+1
        elif itr[2]!=itr[3] and itr[2]!=0:
            print(f"Data: {itr[0]} with key {itr[1]} ->Match in both the files with rows {min(itr[2],itr[3])} but ",end="")
            workbook2.write(workbook2_row, 0, itr[1])
            workbook2.write(workbook2_row, 1, str(itr[0]))
            workbook2.write(workbook2_row, 2, min(itr[2],itr[3]))
            if itr[2]<itr[3]:
                print(f"File 1 has {abs(itr[2]-itr[3])} more rows ")
                workbook2.write(workbook2_row, 3,abs(itr[2]-itr[3]))
                workbook2_row=workbook2_row+1
            else:
                print(f"File 2 has {abs(itr[2] - itr[3])} more rows")
                workbook2.write(workbook2_row, 4, abs(itr[2] - itr[3]))
                workbook2_row = workbook2_row + 1
        elif itr[2]==0:
            print(f"Data: {itr[0]} has only {itr[3]} rows in File 1")
            workbook2.write(workbook2_row, 0, itr[1])
            workbook2.write(workbook2_row, 1, str(itr[0]))
            workbook2.write(workbook2_row, 2, 0)
            workbook2.write(workbook2_row,3,itr[3])
            workbook2_row=workbook2_row+1
    for itr in file_data_2:
        if itr[2]==0:
            print(f"Data: {itr[0]} has only {itr[3]} rows in File 2")
            workbook2.write(workbook2_row, 0, itr[1])
            workbook2.write(workbook2_row, 1, str(itr[0]))
            workbook2.write(workbook2_row, 2, 0)
            workbook2.write(workbook2_row, 4, itr[3])
            workbook2_row = workbook2_row + 1
    report.close()
