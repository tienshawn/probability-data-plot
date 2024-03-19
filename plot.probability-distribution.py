import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas import *
from scipy.stats import gaussian_kde
from numpy import linspace

'''
Reference:
https://stackoverflow.com/a/15418687
'''

# reading CSV file
data_excel1 = read_csv("hey.csv")
data1 = data_excel1['response-time'].tolist()

data_excel2 = read_csv("hey2.csv")
data2 = data_excel2['response-time'].tolist()

#plot the probability distribution
kde1 = gaussian_kde( data1 )
kde2 = gaussian_kde( data2 )
dist_space1 = linspace( min(data1), max(data1), 1000)
dist_space2 = linspace( min(data2), max(data2), 1000)
plt.figure(figsize=(10, 5)) #change the size
plt.plot(dist_space1, kde1(dist_space1), color='blue', label='Data 1')
plt.plot(dist_space2, kde2(dist_space2), color='red', label='Data 2')
plt.xlabel('Data')
plt.ylabel('Probability Density')
plt.title('Probability Distribution of Data')
plt.grid(True)
plt.legend()
plt.show()


