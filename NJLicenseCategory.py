#importing packages
import pandas as pd
import xlrd

def reading_file(file_name):
    #reading the excel file
    applicants = pd.read_excel(file_name)

    #returning the data frame to the main method
    return applicants

def age16(applicants):
    print("the age of this candidate is 16")

    #checking if the list has been correctly received
    print(applicants.shape)

    #checking if the candidate has the driver training enrolled into 1 is true and 0 is false
    print(applicants[:1])

    Driver_training_course_ind = applicants['Driver_training_course_ind']
    Special_learners_permit_ind = applicants['Special_learners_permit_ind']

    if Driver_training_course_ind[0] == '1':
        #checking if he has a special learners permit
        if Special_learners_permit_ind[0] == '1':
            print('you are ready for doing supervised driving ')
    else:
        print('enroll into drivers education')


if __name__=="__main__":
    file_name = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/NJLicenseCategory/NJ License category data set/NJ License applicants data set.xlsx'

    #sending the file name to the reading_file function
    applicants = reading_file(file_name)

    #printing the columns names
    print(applicants[:0])

    #displaying the first record
    print('the first record is:\n ',applicants[:1])

    #converting the Age field to INT
    print("********************************** CONVERTING AGE TO INT ******************************")
    pd.to_numeric(applicants['Age'])
    print("********************************** CONVERSION DONE ******************************")

    #finding out the age of the applicant
    print("********************************** AGE OF THE APPLICANT ******************************")
    age = applicants['Age'][0:]
    print(age[0])


    if age[0] == 16:
        age16(applicants)