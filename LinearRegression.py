import pandas as pd
import numpy as np
import matplotlib.pyplot 
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

filename = 'HonorsData001/LargeData001.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # get counties from this file
    county = []
    highschool = []
    bachelor = []
    female = []
    medianinc = []
    afterinc = []
    for row in reader:
        countynames = (row[0])
        highschoolrate = (row[1])
        bachelorrate = (row[2])
        femalerate = (row[3])
        medianincome = (row[4])
        afterincome = (row[5])
        county.append(countynames)
        highschool.append(highschoolrate)
        bachelor.append(bachelorrate)
        female.append(femalerate)
        medianinc.append(medianincome)
        afterinc.append(afterincome)

# print (county)
# print (highschool)
# print (bachelor)
# print (female)
# print (medianinc)
# print(afterinc)

df = pd.DataFrame({'highschool' : ['88.4', '91.2', '90', '89.2', '90.2', '71.3', '89.5', '80.1', '93.4', '76', '92.8', '90.5', 
'69.7', '88.6', '74.1', '73.4', '85.8', '83.2', '79.1', '71.9', '93.3', '90.6', '86.5', '69.1', '84.8', '88.6', '71.5', '85.5', '94.4', '85.5', '94.5', '95.1', '82', '87.7', '80.5', '80', '87.4', '88.5', '79.3', '91.3', '89.6', '80.9', '88.4', '86.3', '91.1', '92.4', '90.2', '88.4', '88.8', '78.9', '78.2', '84.5', '92.4', '70.8', '90.7', '85', '86.5', '82.3'],
'bachelor' : ['47.4', '34.5', '19.3', '27.2', '18.3', '15', '42.4', '79.7', '34.3', '21.2', '48.2', '30.4', '15.2', '27.2', '16.4', '14.7', '15.5', '12.9', '32.5', '14.6', '59.5', '24.6', '24.4', '13.8', '15.2', '28.8', '24.7', '35.7', '37.2', '40.6', '39.7', '23.7', '22.3', '30.9', '19.7', 
'21', '38.8', '58.1', '18.8', '35.4', '51', '34.2', '52.4', '40.8', '22.2', '17.9', '23.2', '26.9', '35.5', '17.1', '18.2', '15.7', '19.5', '14.6', '20.5', '33.8', '41.4', '17.1'],       
'female' : ['50.7', '46.1', '45.6', '50.5', '50.2', '49.1', '51.1', '45.4', '50.1', '50.1', '49.1', '50.4', '48.7', '49.9', '48.8', '44.9', '50', '37.8', '50.7', '51.8', '51.1', '49.1', '50.4', '49.5', '49.7', '47', '49.1', '50.2', '50.9', '50.7', '51.2', '50.2', '50.1', '51.1', '49.9', '50.2', '49.7', '49', '50.1', '49.4', '50.5', '50', '49.3', '50.5', '50.9', '49.8', '50.3', '50.2', '51.2', '50.4', '50.2', '50.3', '48.6', '50', '48.2', '50.5', '51.5', '49.4'],
'medianinc' : ['92574', '64688', '61198', '48443', '58151', '56704', '93712', '45258', '80582', '51261', '47395', '45528', '45834', '52874', '52479', '53865', '42475', '56362', '64251', '52884', '110217', '51199', '49233', '50129', '45149', '63018', '66676', '84753', '63240', '85398', '84357', '53270', '63948', '63902', '81977', '60164', '74855', '104552', '61145', '70699', '113776', '71657', '116178', '78041', '50905', '48125', '44200', '77609', '76753', '57387', '56955', '42899', '38497', '47518', '56493', '84017', '65923', '52624'],
'afterinc' : ['99406', '63750', '62772', '52537', '63158', '59401', '99716', '45283', '83377', '53969', '49633', '48041', '47622', '57316', '53350', '57848', '47040', '56352', '68044', '57585', '115246', '48820', '51416', '53672', '45507', '62260', '71015', '88596', '66096', '90234', '89691', '55359', '67005', '67151', '86958', '63362', '78980', '112449', '64432', '73518', '122641', '74624', '124055', '82234', '54667', '52418', '45241', '81472', '81018', '60704', '59050', '44514', '40846', '49687', '60108', '88131', '70228', '58054']})

#naming dependent and independent variables
x = df.drop('afterinc', axis=1)
y = ['afterinc']
# splitting the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1, random_state = 58)

#creating an object of LinearRegression class
LR = LinearRegression()
LR.fit(x_train, y_train)

y_prediction = LR.predict(x_test)
print(y_prediction)


