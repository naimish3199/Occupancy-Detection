## Web Application is hosted at https://occupancy-detector-api.herokuapp.com/

#### The aim of this project is to detect human presence in the room(i.e. Occupancy of the room) using Occupancy Detection datasets which is generated using IoT devices installed in the room. We are asked to classify occupancy status in an room i.e. 0 or 1 , 0 for not occupied and 1 for occupied status. There are three datasets given -<br />
* datatraining.txt (For Training) (8143 datapoints)
* datatest.txt (For Testing) (2665 datapoints)  
* datatest2.txt (For Testing) (9752 datapoints)
<br />
Precisely 8143 datapoints are provided for training and 12417 datapoints are provided for testing.<br />


Data contains 6 features -
<br />
* Date time year-month-day hour:minute:second
* Light in Lux 
* CO2 in ppm
* Temperature in Celsius
* Relative Humidity in % 
* Humidity Ratio – No Unit. Derived quantity from temperature and relative humidity

Data contains 1 target variable -

* Occupancy, 0 or 1, 0 for not occupied and 1 for occupied status.
<br />

#### Dataset can be downloaded from https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+ <br />
Supervised learning algorithms used are- 
* Logistic Regression
* Naive Bayes
* K-Nearest Neighbors
* Random Forest
* Support Vector Machine(SVM)
* Artificial Neural Network(ANNs) 
<br />
These algorithms are used after optimization and then performance of these algorithms on testing datasets is analysed.  <br />
<br />
Performance of different classifiers- 

<img width="300" alt="image" src="https://user-images.githubusercontent.com/76880411/146670534-e38b34b9-e784-4780-b8aa-aac01ac5994f.png"> 
<img width="300" alt="image" src="https://user-images.githubusercontent.com/76880411/146670618-5be39b78-62e0-4971-b85b-62861d0d9208.png">

<img width="300" alt="image" src="https://user-images.githubusercontent.com/76880411/146670629-22ae7f04-3851-4717-bc55-cba4986cc4ae.png">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/76880411/146670639-9fff851c-a770-4b31-91d2-7c9796568750.png">











<br />Detailed Analysis is available in Report.
