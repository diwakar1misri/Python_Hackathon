import Report_Generation
def removing_duplicate(file_data_1,file_data_2):
   temp_1_file_1=[]
   temp_2_file_2=[]
   for temp_1_itr in range(0,len(file_data_1)):
       count=0
       for temp_2_itr in range(0,len(file_data_1)):
           if file_data_1[temp_1_itr][0]==file_data_1[temp_2_itr][0] and file_data_1[temp_1_itr][1]==file_data_1[temp_2_itr][1] and file_data_1[temp_1_itr][2]==file_data_1[temp_2_itr][2] and file_data_1[temp_1_itr][3]==file_data_1[temp_2_itr][3]:
               if temp_1_itr<temp_2_itr:
                   count=count+1
       if (count+1)==file_data_1[temp_1_itr][3]:
           temp_1_file_1.append(file_data_1[temp_1_itr])
   file_data_1 = temp_1_file_1[:]
   temp_1_file_1.clear()
   #----------------------------------------------------------------------
   for temp_1_itr in range(0,len(file_data_2)):
       count=0
       for temp_2_itr in range(0,len(file_data_2)):
           if file_data_2[temp_1_itr][0]==file_data_2[temp_2_itr][0] and file_data_2[temp_1_itr][1]==file_data_2[temp_2_itr][1] and file_data_2[temp_1_itr][2]==file_data_2[temp_2_itr][2] and file_data_2[temp_1_itr][3]==file_data_2[temp_2_itr][3]:
               if temp_1_itr<temp_2_itr:
                   count=count+1
       if (count+1)==file_data_2[temp_1_itr][3]:
           temp_2_file_2.append(file_data_2[temp_1_itr])
   file_data_2 = temp_2_file_2[:]
   temp_2_file_2.clear()
   # print(file_data_1)
   # print(file_data_2)
   Report_Generation.Report_Generation(file_data_1,file_data_2)