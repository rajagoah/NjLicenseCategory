#importing packages
import pandas as pd
import xlrd
def data_type_conversion(applicants):
    # converting the following fields to numeric.This conversion is needed so that I can use them in comparison operators
    print("********************************** CONVERTING RELEVANT COLUMNS TO INT *********************************")
    pd.to_numeric(applicants['Age'])
    pd.to_numeric(applicants['Driver_training_course_ind'])
    pd.to_numeric(applicants['Special_learners_permit_ind'])
    pd.to_numeric(applicants['examination_permit_ind'])
    pd.to_numeric(applicants['supervised_driving_ind'])
    pd.to_numeric(applicants['unsupervised_driving_ind'])
    pd.to_numeric(applicants['probationary_license_ind'])
    print("********************************** CONVERSION DONE ******************************")
    return applicants

def reading_file(file_name):
    #reading the excel file
    applicants = pd.read_excel(file_name)

    #returning the data frame to the main method
    return applicants

def age16(applicants, i):
    print("the age of this candidate is 16")

    #checking if the list has been correctly received
    #print(applicants.shape)

    #checking if the candidate has the driver training enrolled into 1 is true and 0 is false
    Driver_training_course_ind = applicants['Driver_training_course_ind']

    Special_learners_permit_ind = applicants['Special_learners_permit_ind']

    #commenting below statements
    #print('Special_learners_permit_ind = ', Special_learners_permit_ind[i],
    #      'Driver_training_course_ind = ', Driver_training_course_ind[i])

    if Driver_training_course_ind[i] == 1:
        print('you have enrolled in to driver training course')
        #checking if he has a special learners permit
        if Special_learners_permit_ind[i] == 1:
            print('you have earnt the special learners permit and have passed the vision test')
            print('you are ready for doing supervised driving ')
    else:
        print('enroll into drivers education')

def age17(applicants, i):
    print("the age of this candidate is 17")

    # checking if the list has been correctly received
    #print(applicants.shape)

    # checking if the candidate has the driver training enrolled into 1 is true and 0 is false
    Driver_training_course_ind = applicants['Driver_training_course_ind']

   # checking if the candidate has the examination permit. 1 is true and 0 if false
    examination_permit_ind = applicants['examination_permit_ind']

   #commenting below print statements
    #print('examination_permit_ind = \n', examination_permit_ind[i],
     #     'Driver_training_course_ind = ', Driver_training_course_ind[i])

    if Driver_training_course_ind[i] == 1:
        # checking if he has a special learners permit
        if examination_permit_ind[i] == 1:
            print('you have earned the examination permit and have passed the vision test.\nyou are ready for doing supervised driving')
        else:
            print('you have to first get the examination permit and clear the vision test')
    else:
        print('enroll into drivers education')

def age18(applicants, i):
    print("the age of this candidate is 18")

    # checking if the list has been correctly received
    #print(applicants.shape)

    # checking if the candidate has the driver training enrolled into 1 is true and 0 is false
    Driver_training_course_ind = applicants['Driver_training_course_ind']

   # checking if the candidate has the examination permit. 1 is true and 0 if false
    examination_permit_ind = applicants['examination_permit_ind']

    # checking if the candidate has the supervised driving. 1 is true and 0 if false
    supervised_driving_ind = applicants['supervised_driving_ind']

    #checking if the candidate has the probationary license indicator set to 1. 1 is true and 0 is false
    probationary_license_ind = applicants['probationary_license_ind']
    # commenting below print statements
    #print('probationary_license_ind = ', probationary_license_ind,
    #      'Driver_training_course_ind = ', Driver_training_course_ind,
    #      'examination_permit_ind = ', examination_permit_ind,
    #      'supervised_driving_ind = ', supervised_driving_ind
    #      )

        # checking if he has a special learners permit
    if examination_permit_ind[i] == 1:
        if probationary_license_ind[i] == 1:
            print('you have had a probationary license.\n you are ready for getting a full license')
        else:
            print('get a probationary license first and then apply for a full license')
    else:
        print('you have to first get the examination permit and clear the vision test')

def decision_tree(applicants):
    try:
        #writing an iterator to call methods per record
        for i in range(len(applicants)):
            print('value of i is: ', i)
            # finding out the age of the applicant
            print("********************************** AGE OF THE APPLICANT ******************************")
            age = applicants['Age'][i]
            print(applicants['Age'][i])

            #decision tree based on the age of the applicant
            if age == 16:
                age16(applicants[i:i+1],i)
            elif age > 16 and age < 18:
                age17(applicants[i:i+1],i)
            elif age == 18:
                age18(applicants[i:i+1],i)
    except IndexError:
        print('********************************** INDEX OUT OF BOUND ERROR **********************************')
    except ValueError:
        print('********************************** VALUE  ERROR **********************************')


if __name__=="__main__":
    file_name = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/NJLicenseCategory/NJ License category data set/NJ License applicants data set.xlsx'

    #sending the file name to the READING FILE METHOD
    applicants = reading_file(file_name)

    #printing the columns names
    print('********************************** COLUMNS IN DATA FRAME **********************************')
    print(applicants[:0])

    #displaying the shape of the data frame
    print('********************************** SHAPE OF DATA FRAME **********************************')
    print(applicants.shape)

    #passing the list of applications to the DATA TYPE CONVERSION METHOD
    applicants = data_type_conversion(applicants)

    #passing the list of applications to the DECISION TREE METHOD
    decision_tree(applicants)