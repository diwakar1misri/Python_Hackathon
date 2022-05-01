import os
import text_file_comparison
import csv_file_comparison
if os.path.exists(os.path.abspath("").replace("Code Scripts","")+"Report_Generated_Summary.xlsx"):
    #print("Already present report deleted")
    os.remove(os.path.abspath("").replace("Code Scripts","")+"Report_Generated_Summary.xlsx")
files_directory=os.path.abspath("").replace("Code Scripts","")+"ComparisonFiles"
#print(files_directory)
list_comp_files=os.listdir(files_directory)
if len(list_comp_files)==2:
    print("Ready to Proceed")
    if (list_comp_files[0][list_comp_files[0].index('.'):]=='.txt' and list_comp_files[1][list_comp_files[0].index('.'):]=='.txt' ):
        print("They both are text file")
        text_file_comparison.text_file_compare(files_directory,list_comp_files[0],list_comp_files[1])
    elif (list_comp_files[0][list_comp_files[0].index('.'):]=='.csv' and list_comp_files[1][list_comp_files[0].index('.'):]=='.csv' ):
        print("They both are csv file")
        csv_file_comparison.csv_comparison(files_directory,list_comp_files[0],list_comp_files[1])
    elif (list_comp_files[0][list_comp_files[0].index('.'):]=='.xlsx' and list_comp_files[1][list_comp_files[0].index('.'):]=='.xlsx' ):
        print("They both are excel file")
    else:
        print("Both are not of the same type")
else:
    print("More than two files")
print("\n\n\n")
print("Report has also been generated in Project_Hackathon folder -->Report_Generated_Summary.xlsx")
input("Press Enter to close the screen")