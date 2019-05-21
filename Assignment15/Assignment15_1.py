from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def checkAccuracy():
	 
	data_train,data_test,target_train,target_test = train_test_split(X,Y,test_size = 0.7)
	
	classifier.fit(data_train,target_train)	
	
	predictions  = classifier.predict(data_test)

	Accuracy = accuracy_score(target_test,predictions)

	print('Accuracy : ',Accuracy*100,"%")


dataset = pd.read_csv('WinePredictor.csv')
X = dataset.iloc[:,1:14]
Y = dataset.iloc[:,0]

#print(X)
#print(Y)

classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X,Y)
x_test = np.array([13.25,1.8,2.3,12.0,101,2.7,2.9,0.28,1.0,4.2,1.10,3.6,1000])
predict = classifier.predict([x_test])
print('RESULT : ',predict)

checkAccuracy()



	
	
