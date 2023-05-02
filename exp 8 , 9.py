Display Image

import cv2

from google.colab import drive

drive.mount('/content/drive')

#importing the opencv module

from google.colab.patches import cv2_imshow

# using imread('path') and 0 denotes read as grayscale image

img = cv2.imread(r'/content/drive/MyDrive/belldanmachi.jpg')

#This is using for display the image

cv2_imshow(img)








Write a program using sklearn machine learning library to study linear regression

import numpy as np

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6]).reshape((-1, 1))

y = np.array([2, 4, 6, 8, 10, 12])

model = LinearRegression()

model.fit(x, y)

x_new = np.array([7, 8, 9, 10, 11]).reshape((-1, 1))

y_new = model.predict(x_new)

print(y_new)

plt.scatter(x, y)

plt.plot(x, model.predict(x), color='red')

plt.scatter(x_new, y_new)

plt.plot(x_new, model.predict(x_new), color = 'blue')

plt.show()








To study multiple linear regression

import pandas as pd

df = pd.read_csv('/content/insurance.csv')

print(df)

#HERE WE HAVE TO PREDICT THE CHARGES

age sex bmi children smoker region charges

0 19 female 27.900 0 yes southwest 16884.92400

1 18 male 33.770 1 no southeast 1725.55230

2 28 male 33.000 3 no southeast 4449.46200

3 33 male 22.705 0 no northwest 21984.47061

4 32 male 28.880 0 no northwest 3866.85520

... ... ... ... ... ... ... ...

1333 50 male 30.970 3 no northwest 10600.54830

1334 18 female 31.920 0 no northeast 2205.98080

1335 18 female 36.850 0 no southeast 1629.83350

1336 21 female 25.800 0 no southwest 2007.94500

1337 61 female 29.070 0 yes northwest 29141.36030

[1338 rows x 7 columns]

df['sex'] = df['sex'].astype('category')

df['sex'] = df['sex'].cat.codes

df['region'] = df['region'].astype('category')

df['region'] = df['region'].cat.codes

df['smoker'] = df['smoker'].astype('category')

df['smoker'] = df['smoker'].cat.codes

print(df)

age sex bmi children smoker region charges

0 19 0 27.900 0 1 3 16884.92400

1 18 1 33.770 1 0 2 1725.55230

2 28 1 33.000 3 0 2 4449.46200

3 33 1 22.705 0 0 1 21984.47061

4 32 1 28.880 0 0 1 3866.85520

... ... ... ... ... ... ... ...

1333 50 1 30.970 3 0 1 10600.54830

1334 18 0 31.920 0 0 0 2205.98080

1335 18 0 36.850 0 0 2 1629.83350

1336 21 0 25.800 0 0 3 2007.94500

1337 61 0 29.070 0 1 1 29141.36030

[1338 rows x 7 columns]

X = df.drop(columns = 'charges')

y = df['charges']

from sklearn.model_selection import *

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)

#from sklearn.model_selection import LinearRegression

lm = LinearRegression()

lm.fit(X_train, y_train)

print(lm.intercept_)

-12460.494204981655

coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])

coeff_df

Coefficient

age 255.051151

sex -314.545735

bmi 357.806148

children 546.477934

smoker 23346.617344

region -360.752248

predictions = lm.predict(X_test)

plt.scatter(y_test,predictions)

lm.score(X_train, y_train)

0.7333103668719112

Logistic Regression

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('/content/Heart.csv')

df['ChestPain'] = df['ChestPain'].astype('category')

df['ChestPain'] = df['ChestPain'].cat.codes

df['Thal'] = df['Thal'].astype('category')

df['Thal'] = df['Thal'].cat.codes

df['AHD'] = df['AHD'].astype('category')

df['AHD'] = df['AHD'].cat.codes

scaler = StandardScaler()

df = df.dropna()

X = df.drop(columns = 'AHD')

y = df['AHD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

log_reg = LogisticRegression(random_state = 0).fit(X_train_scaled, y_train)

log_reg.predict(X_train_scaled)

log_reg.score(X_train_scaled, y_train)

0.8859060402684564

SVM

X_train=np.array([[3, 1],[3, -1],[6, 1],[6, -1],[1,0],[0,1],[0,-1],[-1,0]])

y_train=[1, 1 ,1, 1, 0, 0, 0, 0]

plt.scatter(X_train[:,0], X_train[:,1])

from sklearn import svm

clf = svm.SVC(kernel='linear')

clf = clf.fit(X_train, y_train)

predictions = clf.predict(X_train)

print(predictions)

predictions = clf.predict([[-4,2]])

print(predictions)

support_vectors = clf.support_vectors_

print(support_vectors)

predictions = clf.predict(X_train)

confusion_matrix(y_train, predictions)

clf.score(X_train, predictions)

[1 1 1 1 0 0 0 0]

[0]

[[ 1. 0.]

[ 3. 1.]

[ 3. -1.]]

1.0