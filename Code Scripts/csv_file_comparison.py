import csv
import Common_Compare_data
def csv_comparison(files_directory,file_1_name,file_2_name):
    column_name_key=""
    position_column=0
    file1=open(files_directory+"\\"+file_1_name,"r")
    file2=open(files_directory+"\\"+file_2_name,"r")
    csv_file_1=csv.reader(file1)
    csv_file_2=csv.reader(file2)
    header_1_file=str(next(csv_file_1))[2:][:-2]
    header_2_file=str(next(csv_file_2))[2:][:-2]
    delimiter = input("Enter the delimiter\n")
    key_choice = int(input("Enter \n1. For Position Key\n2. For Name column\n"))
    if key_choice == 1:
        position_column = int(input("Enter the position column:\n")) - 1
    else:
        column_name_key = input("Enter the column name:\n")
    column_names_file_1 = header_1_file.split(delimiter)
    column_names_file_2 = header_2_file.split(delimiter)
    if len(column_names_file_1) == len(column_names_file_2):
        for i in range(0, len(column_names_file_1)):
            if column_names_file_1[i] != column_names_file_2[i]:
                print("Column names do not match")
                return
        if column_name_key != "":
            position_column = column_names_file_1.index(column_name_key)
            print("You choosed key: " + column_name_key)
        else:
            print("You choosed key: " + column_names_file_1[position_column])
    else:
        print("Number of columns do not match")

    file_data_1=[]
    file_data_2=[]

    for itr in csv_file_1:
        file_data_1.append([str(itr)[2:][:-2].split(delimiter),str(itr)[2:][:-2].split(delimiter)[position_column],0,0])
    for itr in csv_file_2:
        file_data_2.append([str(itr)[2:][:-2].split(delimiter),str(itr)[2:][:-2].split(delimiter)[position_column],0,0])
    Common_Compare_data.compare_data(file_data_1,file_data_2)