import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

x, y = [], []
for line_area in open(r'mca_lab1_delta_qsort_area.csv'):
    values = [float(s) for s in line_area.split()]
    x.append(values)
    
for line_cycle in open(r'mca_lab1_delta_qsort_cycles.csv'):
    values = [float(s) for s in line_cycle.split()]
    y.append(values)
    
a, b = [], []
for line_area in open(r'mca_lab1_delta_convolution_area.csv'):
    values = [float(s) for s in line_area.split()]
    a.append(values)
    
for line_cycle in open(r'mca_lab1_delta_convolution_cycle.csv'):
    values = [float(s) for s in line_cycle.split()]
    b.append(values)
    
plt.title('UCBQSORT', fontsize = 20)
plt.xlabel('Delta Area', fontsize=15)
plt.ylabel('Addition Time (Execution Cycles)', fontsize=15)
plt.scatter(x, y, marker='+', s=50, c='red')
plt.show()

plt.title('Convolution_5x5', fontsize = 20)
plt.xlabel('Delta Area', fontsize=15)
plt.ylabel('Addition Time (Execution Cycles)', fontsize=15)
plt.scatter(a, b, marker='+', s=50, c='blue')
plt.show()

plt.title('UCBQSORT VS Convolution_5x5', fontsize = 20)
plt.xlabel('Delta Area', fontsize=15)
plt.ylabel('Addition Time (Execution Cycles)', fontsize=15)
plt.scatter(x, y, marker='+', s=50, c='red')
plt.scatter(a, b, marker='+', s=50, c='blue')
plt.show()