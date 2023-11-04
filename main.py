import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("ds_salaries.csv")
print(data.head())

shape = data.shape
print(shape)

#all columns name
columns = data.columns
print(columns)

#remove first column
data.drop(['Unnamed: 0'],axis=1,inplace=True)


data.drop(['salary_currency','salary'],axis=1,inplace=True)
print(columns)

#Replace feature values for better understandng

data['experience_level'] = data['experience_level'].map({'MI' : 'MID', 'SE': 'SENIOR', 'EN' : 'ENTRY', 'EX': 'EXPERT'})
data['employment_type'] = data['employment_type'].map({ 'PT':'Part-time', 'FT' : 'Full-time', 'CT' : 'Contract', 'FL' : 'Freelance'})
data['remote_ratio'] = data['remote_ratio'].map({0: 'No Remote',50: 'Partially Remote',100: 'Fully Remote'})
data['company_size'] = data['company_size'].map({'L': 'Large','S':'Small','M':'Medium'})

#Check for missing vaues
print(data.isnull().sum())

sns.heatmap(data.isnull())
plt.savefig("heatmap.png")
plt.close()

#Check for duplicates

duplicates = data.duplicated().sum()
print(duplicates)

# Remove duplicate records
data.drop_duplicates(inplace=True)

plt.figure(figsize=(10,5))
sns.boxplot(data=data,x='salary_in_usd')
plt.savefig("salary_in_usd")
plt.close()

#work Year
sns.countplot(data = data, x = "work_year")
plt.savefig("work_year.png")
plt.close()
#Most of the records in the data contains salaries for year 2022.

#Experience level¶
sns.countplot(data = data, x = "experience_level")
plt.savefig("experience_level.png")
plt.close()
#Most of the records are for experience level SE,There are very less records for experience level EX

#Employment Type
sns.countplot(data = data, x = "employment_type")
plt.savefig("employment_type.png")
plt.close()
#Most of the records are for full time employees

#Job Title
sns.countplot(data = data, x = "job_title")
plt.savefig("job_title.png")
plt.close()
#Most popular job titles are Data Scientist,Data Engineer, Data Analyst and Machine learning Engineer


#Employee residence
sns.countplot(data = data, x = "employee_residence")
plt.savefig("employee_residence.png")
plt.close()
#Most of the employees are from US

#Company Location
sns.countplot(data = data, x = "company_location")
plt.savefig("company_location.png")
plt.close()

#Company size
sns.countplot(data = data, x = "company_size")
plt.savefig("company_size.png")
plt.close()

#remote_ratio
sns.countplot(data = data, x = "remote_ratio")
plt.savefig("remote_ratio.png")
plt.close()
#Most emoplyees are working as fully remote


#Multivariate Analysis¶

#1. Which job title earns highest salary ?
job = data.groupby("job_title")["salary_in_usd"].mean()
plt.figure(figsize=(12,16))
sns.barplot(x = job.values, y = job.index)
plt.savefig("plot.png")
plt.close()
#five highest earning jobs are Principal Data Engineer, Principal Data Scientist, Data Architect, Analytics Engineer and Director of Data Science

#2.What is the average salary for each experience level
job = data.groupby("experience_level")["salary_in_usd"].mean()
plt.figure(figsize=(12,16))
sns.barplot(x = job.values, y = job.index)
plt.savefig("plot2.png")
plt.close()
#Average salary of expert is more than other experience levels.


#3. What is the average salary for company size Large, Small and Medium ?

job = data.groupby("company_size")["salary_in_usd"].mean()
plt.figure(figsize=(12,16))
sns.barplot(x = job.values, y = job.index)
plt.savefig("plot3.png")
plt.close()
#On an average employees in large size company earns more


#4. Does people working full time earns more than contract base employees ?

job = data.groupby("employment_type")["salary_in_usd"].mean()
plt.figure(figsize=(12,16))
sns.barplot(x = job.values, y = job.index)
plt.savefig("plot4.png")
plt.close()
#salary of contract base employee is more than full time employee


#5. Is salary less for employee woking remotely than who comes to office ?

job = data.groupby("remote_ratio")["salary_in_usd"].mean()
plt.figure(figsize=(12,16))
sns.barplot(x = job.values, y = job.index)
plt.savefig("plot5.png")
plt.close()
#On an average people working as on remote mode earns more

#6. Which country pays more to the employees ?

job = data.groupby("company_location")["salary_in_usd"].mean()
plt.figure(figsize=(12,16))
sns.barplot(x = job.values, y = job.index)
plt.savefig("plot6.png")
plt.close()
#Top two highest paying countries are Russia and US

#7. Has salary of data science job roles increased over the passing years ?

data_year = data.groupby('work_year')['salary_in_usd'].mean()

plt.figure(figsize=(10,5))
ax = sns.lineplot(x=data_year.index,y=data_year.values)
ax.set_xticks([2020,2021,2022])
ax.set_xlabel('Year')
ax.set_ylabel('Salary')
ax.set_title('Trend in data science job salary over the years')
plt.savefig("plot7.png")
plt.close()

#8. What is the trend of salaries paid by medium size companies over the passing years ?

data_M = data[data['company_size']=='Medium']
data_M_year = data_M.groupby('work_year')['salary_in_usd'].mean()

plt.figure(figsize=(10,5))
ax = sns.lineplot(x=data_M_year.index,y=data_M_year.values)
ax.set_xticks([2020,2021,2022])
ax.set_xlabel('Year')
ax.set_ylabel('Salary')
ax.set_title('Trend in data science job salary over the years for medium size company')
plt.savefig("plot8.png")
plt.close()


#9. What is the trend of salaries paid by large size companies over the passing years ?

data_L = data[data['company_size']=='Large']
data_L_year = data_L.groupby('work_year')['salary_in_usd'].mean()

plt.figure(figsize=(10,5))
ax = sns.lineplot(x=data_L_year.index,y=data_L_year.values)
ax.set_xticks([2020,2021,2022])
ax.set_xlabel('Year')
ax.set_ylabel('Salary')
ax.set_title('Trend in data science job salary over the years for large size company')
plt.savefig("plot9.png")
plt.close()

#10. What is the trend of salaries paid by large size companies over the passing years ?

data_S = data[data['company_size']=='Small']
data_S_year = data_S.groupby('work_year')['salary_in_usd'].mean()

plt.figure(figsize=(10,5))
ax = sns.lineplot(x=data_L_year.index,y=data_L_year.values)
ax.set_xticks([2020,2021,2022])
ax.set_xlabel('Year')
ax.set_ylabel('Salary')
ax.set_title('Trend in data science job salary over the years for small size company')
plt.savefig("plot10.png")
plt.close()