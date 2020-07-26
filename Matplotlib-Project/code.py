# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data = pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()


#Plotting bar plot
loan_status.plot(kind = 'bar')


# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind = 'bar', stacked = False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)

#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()

education_and_loan.plot(kind = 'bar', stacked = 'True')

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation = 45)

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind = 'density', label = 'Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind = 'density', label = 'Not Graduate')

#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1, ax_2, ax_3) = plt.subplots(3, 1)



#Plotting scatter plot
data.plot('ApplicantIncome', 'LoanAmount', kind = 'scatter', ax = ax_1)

#Setting the subplot axis title
ax_1.set_title('Applicant Income')

#Plotting scatter plot
data.plot('CoapplicantIncome', 'LoanAmount', kind = 'scatter', ax = ax_2)

#Setting the subplot axis title
ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot
data.plot('TotalIncome', 'LoanAmount', kind = 'scatter', ax = ax_3)

#Setting the subplot axis title
ax_3.set_title('Total Income')




