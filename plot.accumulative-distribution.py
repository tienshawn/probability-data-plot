# defining the libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
# %matplotlib inline 
from pandas import *

'''
Reference:
https://www.geeksforgeeks.org/how-to-calculate-and-plot-a-cumulative-distribution-function-with-matplotlib-in-python/
'''

# reading CSV file
data_excel1 = read_csv("hey.csv")
data1 = data_excel1['response-time'].tolist()

data_excel2 = read_csv("hey2.csv")
data2 = data_excel2['response-time'].tolist()


# getting data of the histogram 
count1, bins_count1 = np.histogram(data1, bins=10) 
count2, bins_count2 = np.histogram(data2, bins=10) 

# finding the PDF of the histogram using count values 
pdf1 = count1 / sum(count1) 
pdf2 = count2 / sum(count2) 

# using numpy np.cumsum to calculate the Data2 
# We can also find using the PDF values by looping and adding 
cdf1 = np.cumsum(pdf1) 
cdf2 = np.cumsum(pdf2) 

# plotting PDF and CDF 
# plt.plot(bins_count[1:], pdf, color="red", label="PDF") 
plt.plot(bins_count1[1:], cdf1, label="Data1") 
plt.plot(bins_count2[1:], cdf2, label="Data2") 
plt.legend() 
plt.grid(True)
plt.xlabel('Data')
plt.ylabel('Probability')
plt.title('Cumulative Distribution of Data')
plt.show()