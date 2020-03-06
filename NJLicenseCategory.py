#importing packages
import pandas as pd
import xlrd

def reading_file(file_name):
    #reading the excel file
    applicants = pd.read_excel(file_name)

    #returning the data frame to the main method
    return applicants

if __name__=="__main__":
    file_name = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/NJLicenseCategory/NJ License category data set/NJ License applicants data set.xlsx'

    #sending the file name to the reading_file function
    applicants = reading_file(file_name)

    #printing the columns names
    print(applicants[:0])

    #displaying the first record
    print('the first record is: ',applicants[:1])

    #converting the Age field to INT
    print("********************************** CONVERTING AGE TO INT ******************************")
    pd.to_numeric(applicants['Age'])

    #finding out the age of the applicant
    print("********************************** AGE OF THE APPLICANT ******************************")
    age = applicants['Age'][0:]
    print(age)