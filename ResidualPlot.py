import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sklearn 
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split as tts
import yellowbrick
from yellowbrick.datasets import load_concrete
from yellowbrick.regressor import residuals_plot
from yellowbrick.regressor import ResidualsPlot

#highschool residual: load dataset and split

X, y = load_concrete([88.4, 91.2, 90, 89.2, 90.2, 71.3, 89.5, 80.1, 93.4, 76, 92.8, 90.5, 69.7, 88.6, 74.1, 73.4, 85.8, 83.2, 79.1, 71.9, 93.3, 90.6, 86.5, 69.1, 84.8, 88.6, 71.5, 85.5, 94.4, 85.5, 94.5, 95.1, 82, 87.7, 80.5, 80, 87.4, 88.5, 79.3, 91.3, 89.6, 80.9, 88.4, 86.3, 91.1, 92.4, 90.2, 88.4, 88.8, 78.9, 78.2, 84.5, 92.4, 70.8, 90.7, 85, 86.5, 82.3], [99406, 63750, 62772, 52537, 63158, 59401, 99716, 45283, 83377, 53969, 49633, 48041, 47622, 57316, 53350, 57848, 47040, 56352, 68044, 57585, 115246, 48820, 51416, 53672, 45507, 62260, 71015, 88596, 66096, 90234, 89691, 55359, 67005, 67151, 86958, 63362, 78980, 112449, 64432, 73518, 122641, 74624, 124055, 82234, 54667, 52418, 45241, 81474, 81018, 60704, 59050, 44514, 40846, 49687, 60108, 88131, 70228, 58054])
X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.2, shuffle = True)
model = Ridge()
visualizer = ResidualsPlot(model)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
visualizer.show() 
#Create the visualizer, fit, score, and show it
# viz = residuals_plot(RandomForestRegressor(), X_train, y_train, X_test, y_test)
# viz

#bachelor residual: load dataset and split

x1, y1 = load_concrete([47.4, 34.5, 19.3, 27.2, 18.3, 15, 42.4, 79.7, 34.3, 21.2, 48.2, 30.4, 15.2, 27.2, 16.4, 14.7, 15.5, 12.9, 32.5, 14.6, 59.5, 24.6, 24.4, 13.8, 15.2, 28.8, 24.7, 35.7, 37.2, 40.6, 39.7, 23.7, 22.3, 30.9, 19.7, 
21, 38.8, 58.1, 18.8, 35.4, 51, 34.2, 52.4, 40.8, 22.2, 17.9, 23.2, 26.9, 35.5, 17.1, 18.2, 15.7, 19.5, 14.6, 20.5, 33.8, 41.4, 17.1], [99406, 63750, 62772, 52537, 63158, 59401, 99716, 45283, 83377, 53969, 49633, 48041, 47622, 57316, 53350, 57848, 47040, 56352, 68044, 57585, 115246, 48820, 51416, 53672, 45507, 62260, 71015, 88596, 66096, 90234, 89691, 55359, 67005, 67151, 86958, 63362, 78980, 112449, 64432, 73518, 122641, 74624, 124055, 82234, 54667, 52418, 45241, 81474, 81018, 60704, 59050, 44514, 40846, 49687, 60108, 88131, 70228, 58054])
x1_train, x1_test, y1_train, y1_test = tts(x1, y1, test_size = 0.2, shuffle = True)
model1 = Ridge()
visualizer1 = ResidualsPlot(model1)

visualizer1.fit(x1_train, y_train)  # Fit the training data to the visualizer1
visualizer1.score(x1_test, y_test)  # Evaluate the model on the test data
visualizer1.show()

#female residual

x2, y2 = load_concrete([50.7, 46.1, 45.6, 50.5, 50.2, 49.1, 51.1, 45.4, 50.1, 50.1, 49.1, 50.4, 48.7, 49.9, 48.8, 44.9, 50, 47.8, 50.7, 51.8, 51.1, 49.1, 50.4, 49.5, 49.7, 47, 49.1, 50.2, 50.9, 50.7, 51.2, 50.2, 50.1, 51.1, 49.9, 50.2, 49.7, 49, 50.1, 49.4, 50.5, 50, 49.3, 50.5, 50.9, 49.8, 50.3, 50.2, 51.2, 50.4, 50.2, 50.3, 48.6, 50, 48.2, 50.5, 51.5, 49.4],[99406, 63750, 62772, 52537, 63158, 59401, 99716, 45283, 83377, 53969, 49633, 48041, 47622, 57316, 53350, 57848, 47040, 56352, 68044, 57585, 115246, 48820, 51416, 53672, 45507, 62260, 71015, 88596, 66096, 90234, 89691, 55359, 67005, 67151, 86958, 63362, 78980, 112449, 64432, 73518, 122641, 74624, 124055, 82234, 54667, 52418, 45241, 81474, 81018, 60704, 59050, 44514, 40846, 49687, 60108, 88131, 70228, 58054])
x2_train, x2_test, y2_train, y2_test = tts(x2, y2, test_size = 0.2, shuffle = True)
model2 = Ridge()
visualizer2 = ResidualsPlot(model2)
visualizer2.fit(x1_train, y_train)  # Fit the training data to the visualizer2
visualizer2.score(x1_test, y_test)  # Evaluate the model on the test data
visualizer2.show()
#medianinc residual 

x3, y3 = load_concrete([92574, 64688, 61198, 48443, 58151, 56704, 93712, 45258, 80582, 51261, 47395, 45528, 45834, 52874, 52479, 53865, 42475, 56362, 64251, 52884, 110217, 51199, 49233, 50129, 45149, 63018, 66676, 84753, 63240, 85398, 84354, 53270, 63948, 63902, 81977, 60164, 74855, 104552, 61145, 70699, 113776, 71657, 116178, 78041, 50905, 48125, 44200, 77609, 76753, 57387, 56955, 42899, 38497, 47518, 56493, 84017, 65923, 52624], [99406, 63750, 62772, 52537, 63158, 59401, 99716, 45283, 83377, 53969, 49633, 48041, 47622, 57316, 53350, 57848, 47040, 56352, 68044, 57585, 115246, 48820, 51416, 53672, 45507, 62260, 71015, 88596, 66096, 90234, 89691, 55359, 67005, 67151, 86958, 63362, 78980, 112449, 64432, 73518, 122641, 74624, 124055, 82234, 54667, 52418, 45241, 81474, 81018, 60704, 59050, 44514, 40846, 49687, 60108, 88131, 70228, 58054])
x3_train, x3_test, y3_train, y3_test = tts(x3, y3, test_size = 0.2, shuffle = True)
model3 = Ridge()
visualizer3 = ResidualsPlot(model3)
visualizer3.fit(x1_train, y_train)  # Fit the training data to the visualizer3
visualizer3.score(x1_test, y_test)  # Evaluate the model on the test data
visualizer3.show()


