# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.array([[50,  9,  4,  1,  0,  0, 40,  0]])
print(new_record)
print(new_record.shape)
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
#Code starts here
census = np.concatenate((data,new_record))
print(census.shape)

#Taking age column from census
age = census[:,0]
print(age)

#Finding max, min, mean, and standard deviation
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)
print(age_std)

#Taking age column from census
race = census[:, 2]

#Finding race equals to 0, 1, 2, 3, 4
race_0 = race[race == 0]
race_1 = race[race == 1]
race_2 = race[race == 2]
race_3 = race[race == 3]
race_4 = race[race == 4]

#Length of race arrays
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#Finding array index with min value
len_array = np.array([len_0, len_1, len_2, len_3, len_4])
minority_race = np.argmin(len_array)
print(minority_race)

#Creating senior_citizens array with age > 60
senior_citizens = census[census[:, 0] > 60]

#Finding sum of working hours of senior_citizens array
working_hours_sum = senior_citizens[:,6].sum()

#length of senior_citizens array
senior_citizens_len = len(senior_citizens)

#Average working hours of senior citizens
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

high = census[census[:, 1] > 10]
low = census[census[:, 1] <= 10]

avg_pay_high = high[:, 7].mean()
avg_pay_low = low[:, 7].mean()
print(avg_pay_high)
print(avg_pay_low)


