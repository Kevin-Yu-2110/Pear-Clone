# Support Vector 

import datetime
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from models.clean_up import clean_up


data = pd.read_csv('fraudTrain.csv')
features = ['trans_date_trans_time', 'cc_num', 'merchant', 'category', 'amt', 'city', 'job', 'dob', 'is_fraud']
data = data[features]
data.dropna(ignore_index=True)
x_train = data.iloc[:, :-1]
y_train = data.iloc[:, -1:]

encoder = LabelEncoder()
x_train = clean_up(x_train, encoder)[0]

model = SVC()
model.fit(x_train, y_train)

test = pd.read_csv('fraudTest.csv')
test = test[features]
x_test = test.iloc[:, :-1]
y_test = test.iloc[:, -1:]

x_test = clean_up(x_test, encoder)[0]

preds = model.predict(x_test)
accuracy_score(preds, y_test)

confusion_matrix(y_test, preds)