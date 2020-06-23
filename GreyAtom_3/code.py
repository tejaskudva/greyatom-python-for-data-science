# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record = [[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.array(np.genfromtxt(path, delimiter=",", skip_header=1))

#Code starts here
census = np.concatenate((data, new_record))
print(data.shape)
print(census.shape)

age = (census[:,0])
print(age)
max_age = max(age)
min_age = min(age)
age_mean = sum(age) / len(age)
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority = [len_0, len_1, len_2, len_3, len_4]
small = min(minority)
minority_race = minority.index(small)

print(minority_race)

senior_citizens = census[census[:,0] > 60]
working_hours_sum = senior_citizens.sum(axis=0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print(working_hours_sum)
print(avg_working_hours)

high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]

avg_pay_high = high.mean(axis=0)[7]
print(avg_pay_high)

avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_low)













