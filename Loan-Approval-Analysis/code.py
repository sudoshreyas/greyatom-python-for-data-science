# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

# Creating bank dataframe from bank_data
bank = pd.DataFrame(bank_data)


# Selecting categorical data from dataframe
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.shape)

# Selecting numerical data from dataframe
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.shape)

# Creating a new dataframe banks from bank by dropping column Loan_ID from bak
banks = bank.drop(['Loan_ID'], axis = 1)
print(banks.shape)

# Calculating mode for banks dataframe
bank_mode = banks.mode()

# Filling NaN values of dataframe with mode 
#banks.fillna(bank_mode, inplace=True)
banks.replace(np.nan, bank_mode, inplace=True)
print(banks.isnull().sum().values.sum())

# Creating pivot table for calculating average loan amount
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1],2)

loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])

loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
percentage_se = (loan_approved_se*100)/614
print(percentage_se)
percentage_nse = (loan_approved_nse*100)/614
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
loan_term = pd.DataFrame(loan_term)
big_loan_term = len(loan_term[loan_term['Loan_Amount_Term']>=25])
print(big_loan_term)

 
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']

mean_values=loan_groupby.agg([np.mean])
print(mean_values)


