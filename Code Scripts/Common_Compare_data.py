# import pandas
import removing_duplicates
def compare_data(file_data_1,file_data_2):
    if isinstance(file_data_1,list) and isinstance(file_data_2,list):
        # print(file_data_1)
        # print(file_data_2)

        # ----------------1 st file comparison----with respect to 2nd file----------------------------------------------
        for file_1_itr in range(0,len(file_data_1)):
            for file_2_itr in range(0,len(file_data_2)):
                if file_data_1[file_1_itr][1]==file_data_2[file_2_itr][1]:
                    flag=0
                    for row_itr in range(0,len(file_data_1[file_1_itr][0])):
                            if file_data_1[file_1_itr][0][row_itr]!=file_data_2[file_2_itr][0][row_itr]:
                                flag=1
                                break
                            # else:
                            #     print(file_data_1[file_1_itr][0][row_itr]+" "+file_data_2[file_2_itr][0][row_itr])
                    if flag==0:
                        file_data_1[file_1_itr][2]=file_data_1[file_1_itr][2]+1
#----------------2 nd file comparison----with respect to 1st file----------------------------------------------
        for file_2_itr in range(0,len(file_data_2)):
            for file_1_itr in range(0,len(file_data_1)):
                if file_data_2[file_2_itr][1]==file_data_1[file_1_itr][1]:
                    flag=0
                    for row_itr in range(0,len(file_data_1[file_1_itr][0])):
                            if file_data_1[file_1_itr][0][row_itr]!=file_data_2[file_2_itr][0][row_itr]:
                                flag=1
                                break
                            # else:
                            #     print(file_data_2[file_2_itr][0][row_itr]+" "+file_data_1[file_1_itr][0][row_itr])
                    if flag==0:
                        file_data_2[file_2_itr][2]=file_data_2[file_2_itr][2]+1
#-----------------------------1st file data frequency--------------------------------------------------
        for file_1_itr_1 in range(0, len(file_data_1)):
            for file_1_itr_2 in range(0,len(file_data_1)):
                if file_data_1[file_1_itr_1][1]==file_data_1[file_1_itr_2][1]:
                    flag=0
                    for itr in range(0,len(file_data_1[file_1_itr_1][0])):
                        # print(f"{file_1_itr_1}{itr} {file_data_1[file_1_itr_1][0][itr]}  {file_1_itr_2}{itr}  {file_data_1[file_1_itr_2][0][itr]}")
                        if file_data_1[file_1_itr_1][0][itr]!=file_data_1[file_1_itr_2][0][itr]:
                            flag=1
                            break
                    if flag==0:
                        file_data_1[file_1_itr_1][3]=file_data_1[file_1_itr_1][3]+1
    # -----------------------------2st file data frequency--------------------------------------------------
        for file_2_itr_1 in range(0, len(file_data_2)):
            for file_2_itr_2 in range(0,len(file_data_2)):
                if file_data_2[file_2_itr_1][1]==file_data_2[file_2_itr_2][1]:
                    flag=0
                    for itr in range(0,len(file_data_2[file_2_itr_1][0])):
                        if file_data_2[file_2_itr_1][0][itr]!=file_data_2[file_2_itr_2][0][itr]:
                            flag=1
                            break
                    if flag==0:
                        file_data_2[file_2_itr_1][3]=file_data_2[file_2_itr_1][3]+1
    else:
        raise Exception("Got some other data type")

    # print(pandas.DataFrame(file_data_1))
    # print("---------------------------------------------------------")
    # print(pandas.DataFrame(file_data_2))
    removing_duplicates.removing_duplicate(file_data_1,file_data_2)