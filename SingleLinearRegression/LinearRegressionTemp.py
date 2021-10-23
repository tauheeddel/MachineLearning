import sklearn
import numpy as np
import matplotlib.pyplot as plt

# F = 1.8*C + 32
# y = mx + c
x = list(range(0, 39))   #C
# List Comprehension is a for loop in one line
y = [1.8*F + 32 for F in x]
print(f'X: {x}')
print(f'Y: {y}')


plt.plot(x, y, '-*r')
plt.show()


