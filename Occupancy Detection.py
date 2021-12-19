#importing libraries
import numpy as np
import pandas as pd
import pickle
import sklearn
#loading dataset

df = pd.read_csv("C:/Users/naimi/OneDrive/Desktop/PL/Projects/OccupancyDetection/DataSet/datatraining.txt")
df = df.drop(['date'], axis = 1)                    


# Defining features and target variable
X = df[['Temperature','Humidity','Light','CO2','HumidityRatio']]
Y = df['Occupancy']

					
from sklearn.naive_bayes import GaussianNB
GNB = GaussianNB()
# Model Fitting
GNB.fit(X,Y)
#Dumping the model with use of pickle
pickle.dump(GNB,open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[23,27,426,704,0.004]]))