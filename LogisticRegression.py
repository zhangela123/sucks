import pandas as pd
import numpy as np
from sklearn import preprocessing
import statsmodels.api as sm
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import seaborn as sns
from imblearn.over_sampling import SMOTE

sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

df = pd.DataFrame({'highschool' : ['88.4', '91.2', '90', '89.2', '90.2', '71.3', '89.5', '80.1', '93.4', '76', '92.8', '90.5', 
'69.7', '88.6', '74.1', '73.4', '85.8', '83.2', '79.1', '71.9', '93.3', '90.6', '86.5', '69.1', '84.8', '88.6', '71.5', '85.5', '94.4', '85.5', '94.5', '95.1', '82', '87.7', '80.5', '80', '87.4', '88.5', '79.3', '91.3', '89.6', '80.9', '88.4', '86.3', '91.1', '92.4', '90.2', '88.4', '88.8', '78.9', '78.2', '84.5', '92.4', '70.8', '90.7', '85', '86.5', '82.3'],
'bachelor' : ['47.4', '34.5', '19.3', '27.2', '18.3', '15', '42.4', '79.7', '34.3', '21.2', '48.2', '30.4', '15.2', '27.2', '16.4', '14.7', '15.5', '12.9', '32.5', '14.6', '59.5', '24.6', '24.4', '13.8', '15.2', '28.8', '24.7', '35.7', '37.2', '40.6', '39.7', '23.7', '22.3', '30.9', '19.7', 
'21', '38.8', '58.1', '18.8', '35.4', '51', '34.2', '52.4', '40.8', '22.2', '17.9', '23.2', '26.9', '35.5', '17.1', '18.2', '15.7', '19.5', '14.6', '20.5', '33.8', '41.4', '17.1'],       
'female' : ['50.7', '46.1', '45.6', '50.5', '50.2', '49.1', '51.1', '45.4', '50.1', '50.1', '49.1', '50.4', '48.7', '49.9', '48.8', '44.9', '50', '37.8', '50.7', '51.8', '51.1', '49.1', '50.4', '49.5', '49.7', '47', '49.1', '50.2', '50.9', '50.7', '51.2', '50.2', '50.1', '51.1', '49.9', '50.2', '49.7', '49', '50.1', '49.4', '50.5', '50', '49.3', '50.5', '50.9', '49.8', '50.3', '50.2', '51.2', '50.4', '50.2', '50.3', '48.6', '50', '48.2', '50.5', '51.5', '49.4'],
'medianinc' : ['92574', '64688', '61198', '48443', '58151', '56704', '93712', '45258', '80582', '51261', '47395', '45528', '45834', '52874', '52479', '53865', '42475', '56362', '64251', '52884', '110217', '51199', '49233', '50129', '45149', '63018', '66676', '84753', '63240', '85398', '84357', '53270', '63948', '63902', '81977', '60164', '74855', '104552', '61145', '70699', '113776', '71657', '116178', '78041', '50905', '48125', '44200', '77609', '76753', '57387', '56955', '42899', '38497', '47518', '56493', '84017', '65923', '52624'],
'afterinc' : ['1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']})

data = pd.read_csv('HonorsData001/LargeData001.csv', header=0)
data = data.dropna()
print(data.shape)
print(list(data.columns))
data.head()

x = data.loc[:, data.columns != 'afterinc']
y = data.loc[:, data.columns == 'y']

os = SMOTE(random_state=0)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
columns = x_train.columns

os_data_x,os_data_y=os.fit_sample(x_train, y_train)
os_data_x = pd.DataFrame(data=os_data_x,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['y'])
#Check the numbers of data
print("length of oversampled data is ",len(os_data_x))
print("Number of no subscription in oversampled data",len(os_data_y[os_data_y['y']==0]))
print("Number of subscription",len(os_data_y[os_data_y['y']==1]))
print("Proportion of no subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==0])/len(os_data_x))
print("Proportion of subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==1])/len(os_data_x))

#Recursive Feature Elimination
data_vars=data.columns.values.tolist()
y=['y']
x=[i for i in data_vars if i not in y]

logreg = LogisticRegression()
rfe = RFE(logreg, 20)
rfe = rfe.fit(os_data_x, os_data_y.values.ravel())
# print(rfe.support_)
# print(rfe.ranking_)

cols=['highschool', 'bachelor', 'female', 'medianinc', "result_increase", "result_decrease"] 
x=os_data_x[cols]
y=os_data_y['y']

logit_model = sm.Logit(y,x)
finalresult = logit_model.fit()
print(finalresult.summary2())

#model fitting
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
print(logreg.fit(x_train, y_train))

#accuracy of modeling equation
y_pred = logreg.predict(x_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(x_test, y_test)))



