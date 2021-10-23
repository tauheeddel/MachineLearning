import random
import sklearn
import numpy as np
import matplotlib.pyplot as plt

from sklearn import model_selection
from sklearn import linear_model

# F = 1.8*C + 32
# y = mx + c
x = list(range(0, 10))   #C
# List Comprehension is a for loop in one line
y = [1.8*F + 32 for F in x]
#y = [1.8*F + 32 + random.randint(-3,3) for F in x]
print(f'X: {x}')
print(f'Y: {y}')


plt.plot(x, y, '-*r')
plt.show()

x =np.array(x).reshape(-1,1)
y =np.array(y).reshape(-1,1)

xTrain, xTest, yTrain, yTest = model_selection.train_test_split(x,y, test_size=0.2)
model = linear_model.LinearRegression()
model.fit(xTrain, yTrain)
print(f'Coeeficent: {model.coef_}')
print(f'Intercept: {model.intercept_}')

accuracy = model.score(xTest, yTest)
print(f'Accuracy: {round(accuracy*100,2)}')

