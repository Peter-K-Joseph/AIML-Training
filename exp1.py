import pandas as pd

datasheet = pd.read_csv('datasheet.csv')

print(datasheet)

print("Average age: {0}".format(round(datasheet['Age'].mean())))

print("Average salary: {0}".format(round(datasheet['Salary'].mean(), 2)))
print("Sum of all salaries: {0}".format(round(datasheet['Salary'].sum(), 2)))
print("Maximum salary: {0}".format(round(datasheet['Salary'].max(), 2)))
print("Minimum salary: {0}".format(round(datasheet['Salary'].min(), 2)))
print("Standard deviation of salaries: {0}".format(round(datasheet['Salary'].std(), 2)))
print("Variance of salaries: {0}".format(round(datasheet['Salary'].var(), 2)))
print("Number of rows: {0}".format(datasheet.shape[0]))
