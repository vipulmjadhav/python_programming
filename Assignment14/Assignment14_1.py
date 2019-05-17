from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

def checkAccuracy(classifier,x,y):

	data_train,data_test,target_train,target_test = train_test_split(x.iloc[:,1:3],y,test_size = 0.5)
	
	classifier.fit(data_train,target_train)	
	
	predictions  = classifier.predict(data_test)

	Accuracy = accuracy_score(target_test,predictions)

	print('Accuracy : ',Accuracy*100,"%")


def MLKnn():

	#step 1 : loading of data using pandas

	dataset = pd.read_csv("PlayPredictor.csv")

	#step 2 : clean , prepare , manipulate - LabelEncoder()

	x = dataset.iloc[:,:-1]         #selects all colums except last which is target
	y = dataset.iloc[:,3].values    # selects only the target column
	x = x.apply(LabelEncoder().fit_transform)
	print(x)

	#step 3 : train data , KNN and using fit 

	classifier = KNeighborsClassifier(n_neighbors = 3)
	classifier.fit(x.iloc[:,1:3],y)

	#step 4 : test data

	#weather: (overcast = 0 , rainy = 1 , sunny = 2)   By LabelEncoder
	#temp = (cool = 0 , hot = 1 , mild = 2)            By LabelEncoder

	weather = input('Enter Weather (overcast,rainy,sunny): ')
	temp = input('Enter temperature (cool,hot,mild): ')

	if(weather.lower() == 'overcast'):
		weather = 0
	elif(weather.lower() == 'rainy'):
		weather = 1
	elif(weather.lower() == 'sunny'):
		weather = 2

	if(temp.lower() == 'cool'):
		temp = 0	
	elif(temp.lower() == 'hot'):
		temp = 1
	elif(temp.lower() == 'mild'):
		temp = 2
		
	#print(weather," ",temp)
		
	pred_in = ([weather,temp])

	predictions = classifier.predict([pred_in])

	print('Plays : ',predictions)

	#step 5 : calculates accuracy
	
	checkAccuracy(classifier,x,y)

if __name__ == "__main__":
	MLKnn()
