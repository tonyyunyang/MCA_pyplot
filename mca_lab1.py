import pandas as pd
import matplotlib.pyplot as plt
import csv

# with open(r'C:\Users\tonyy\Desktop\python_plot\mca_lab1_ucbqsort_area.csv') as f:
#     for line in f:
#         print(line)

x, y = [], []
for line_area in open(r'mca_lab1_ucbqsort_area.csv'):
    values = [float(s) for s in line_area.split()]
    x.append(values)
    
for line_cycle in open(r'mca_lab1_ucbqsort_excycles.csv'):
    values = [float(s) for s in line_cycle.split()]
    y.append(values)
    
a, b = [], []
for line_area in open(r'mca_lab1_convolution_area.csv'):
    values = [float(s) for s in line_area.split()]
    a.append(values)
    
for line_cycle in open(r'mca_lab1_convolution_excycles.csv'):
    values = [float(s) for s in line_cycle.split()]
    b.append(values)
    
plt.title('UCBQSORT', fontsize = 20)
plt.xlabel('Area', fontsize=15)
plt.ylabel('Time (Execution Cycles)', fontsize=15)
plt.scatter(x, y, marker='+', s=50, c='red')
plt.show()

plt.title('Convolution_5x5', fontsize = 20)
plt.xlabel('Area', fontsize=15)
plt.ylabel('Time (Execution Cycles)', fontsize=15)
plt.scatter(a, b, marker='+', s=50, c='blue')
plt.show()
    
plt.title('UCBQSORT VS Convolution_5x5', fontsize = 20)
plt.xlabel('Area', fontsize=15)
plt.ylabel('Time (Execution Cycles)', fontsize=15)
plt.scatter(x, y, marker='+', s=50, c='red')
plt.scatter(a, b, marker='+', s=50, c='blue')
plt.show()