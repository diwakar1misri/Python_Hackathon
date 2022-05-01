import Common_Compare_data
def text_file_compare(directory,file1,file2):
    position_column=0
    column_name_key=""
    file_1=open(directory+"\\"+file1,"r")
    file_2=open(directory+"\\"+file2,"r")
    delimiter=input("Enter the delimiter\n")
    key_choice=int(input("Enter \n1. For Position Key\n2. For Name column\n"))
    if key_choice==1:
        position_column=int(input("Enter the position column:\n"))-1
    else:
        column_name_key=input("Enter the column name:\n")
    column_names_file_1=file_1.readline().split(delimiter)
    column_names_file_2=file_2.readline().split(delimiter)
    if len(column_names_file_1)==len(column_names_file_2):
        for i in range(0,len(column_names_file_1)):
            if column_names_file_1[i]!=column_names_file_2[i]:
                print("Column names do not match")
                return
        if column_name_key!="":
            position_column=column_names_file_1.index(column_name_key)
            print("You choosed key: "+column_name_key)
        else:
            print("You choosed key: "+column_names_file_1[position_column])
    else:
        print("Number of columns do not match")

    file_data_1=[]
    file_data_2=[]
    for file_data_reader in file_1:
        file_data_1.append([file_data_reader.split(delimiter),file_data_reader.split(delimiter)[position_column],0,0])
    for file_data_reader in file_2:
        file_data_2.append([file_data_reader.split(delimiter),file_data_reader.split(delimiter)[position_column],0,0])
    file_1.close()
    file_2.close()
    Common_Compare_data.compare_data(file_data_1,file_data_2)
    