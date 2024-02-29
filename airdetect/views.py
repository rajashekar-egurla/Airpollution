from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import itertools
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import PassiveAggressiveClassifier
import os
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Create your views here.
def home(request):
	return render(request,'index.html')

def nvb(request):
	return render(request,'pacweb1.html')

def pac(request):
	if request.method == 'POST':
		if request.method == 'POST':
			headline1= request.POST.get('headline1')
			headline2= request.POST.get('headline2')
			headline3= request.POST.get('headline3')
			headline4= request.POST.get('headline4')
			headline5= request.POST.get('headline5')
			headline6= request.POST.get('headline6')
			headline7= request.POST.get('headline7')

			print(headline1)
			
			
			headline1= int(headline1)
			headline2 = int(headline2)
			headline3 = int(headline3)
			headline4 = headline4
			headline5 = float(headline5)
			headline6 = float(headline6)
			headline7 = int(headline7)	
	
			#headline8 = int(headline8)
			from django.shortcuts import render
			from django.http import HttpResponse
			import pandas as pd
			import numpy as np
			import matplotlib.pyplot as plt
			from sklearn.model_selection import train_test_split
			from sklearn.feature_extraction.text import TfidfVectorizer
			import itertools
			from sklearn import metrics
			import os
			import seaborn as sns
			from sklearn.model_selection import train_test_split
			from sklearn.metrics import confusion_matrix
			df = pd.read_csv(r'C:\Users\sarka\Desktop\mini\Airpolution\pollution.csv')
			df1=df.fillna(0)
			from sklearn.preprocessing import LabelEncoder
			le = LabelEncoder()
			le
			dfle = df1.copy()
			dfle
			'''dfle.Name = le.fit_transform(dfle.Name)
			dfle.Location = le.fit_transform(dfle.Location)
			dfle.Fuel_Type = le.fit_transform(dfle.Fuel_Type)'''
			dfle.wnd_dir = le.fit_transform(dfle.wnd_dir)
			headline4 = le.fit_transform([[headline4]])
			#dfle.Mileage = le.fit_transform(dfle.Mileage)
			#dfle.Engine = le.fit_transform(dfle.Engine)
			dfle
			print(dfle)
			X = dfle[['dew','temp','press','wnd_dir','wnd_spd','snow','rain']].values
			X
			y = dfle[['pollution']]
			y
			atest=[[headline1,headline2,headline3,headline4,headline5,headline6,headline7]]
			#train_test separation
			X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
			from sklearn.ensemble import RandomForestRegressor
			regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
			regressor.fit(X_train, y_train)
			pred = regressor.predict(X_test)
			pred1 = regressor.predict(atest)
			print(pred)
			print(pred1)
			print(regressor.score(X_train, y_train))
			d={'predictedvalue':pred1,'accuracy':regressor.score(X_train, y_train)}				 
	return render(request,'result.html',d)

def svm(request):	
	return render(request,'acc1.html')

def dec(request):
	from django.shortcuts import render
	from django.http import HttpResponse
	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	import itertools
	from sklearn import metrics
	import os
	import seaborn as sns
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import confusion_matrix
	df = pd.read_csv(r'C:\Users\sarka\Desktop\mini\Airpolution\pollution.csv')
	df1=df.fillna(0)
	from sklearn.preprocessing import LabelEncoder
	le = LabelEncoder()
	le
	dfle = df1.copy()
	dfle
	'''dfle.Name = le.fit_transform(dfle.Name)
	dfle.Location = le.fit_transform(dfle.Location)
	dfle.Fuel_Type = le.fit_transform(dfle.Fuel_Type)'''
	dfle.wnd_dir = le.fit_transform(dfle.wnd_dir)
	SE = le.fit_transform([['SE']])
	#dfle.Mileage = le.fit_transform(dfle.Mileage)
	#dfle.Engine = le.fit_transform(dfle.Engine)
	dfle
	print(dfle)
	X = dfle[['dew','temp','press','wnd_dir','wnd_spd','snow','rain']].values
	X
	y = dfle[['pollution']]
	y
	atest=[[-16,-4,1020,SE,1.79,0,0]]
	#train_test separation
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
	from sklearn.linear_model import LinearRegression
	linear_clf1 = LinearRegression()
	from sklearn.ensemble import RandomForestRegressor
	linear_clf = RandomForestRegressor(n_estimators = 100, random_state = 0)
	linear_clf.fit(X_train, y_train)
	pred = linear_clf.predict(X_test)
	pred1 = linear_clf.predict(atest)
	print(pred)
	print(pred1)
	print(linear_clf.score(X_train, y_train))
	d={'accuracy':linear_clf.score(X_train, y_train)}
	return render(request,'acc1.html',d)

def randomf(request):
	from django.shortcuts import render
	from django.http import HttpResponse
	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	import itertools
	from sklearn import metrics
	import os
	import seaborn as sns
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import confusion_matrix
	df = pd.read_csv(r'C:\Users\sarka\Desktop\mini\Airpolution\pollution.csv')
	df1=df.fillna(0)
	from sklearn.preprocessing import LabelEncoder
	le = LabelEncoder()
	le
	dfle = df1.copy()
	dfle
	'''dfle.Name = le.fit_transform(dfle.Name)
	dfle.Location = le.fit_transform(dfle.Location)
	dfle.Fuel_Type = le.fit_transform(dfle.Fuel_Type)'''
	dfle.wnd_dir = le.fit_transform(dfle.wnd_dir)
	SE = le.fit_transform([['SE']])
	#dfle.Mileage = le.fit_transform(dfle.Mileage)
	#dfle.Engine = le.fit_transform(dfle.Engine)
	dfle
	print(dfle)
	X = dfle[['dew','temp','press','wnd_dir','wnd_spd','snow','rain']].values
	X
	y = dfle[['pollution']]
	y
	
	atest=[[-16,-4,1020,SE,1.79,0,0]]
	#train_test separation
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
	from sklearn import linear_model
	linear_clf = linear_model.ElasticNet()
	linear_clf.fit(X_train, y_train)
	pred = linear_clf.predict(X_test)
	#pred1 = linear_clf.predict(atest)
	print(pred)
	#print(pred1)
	print(linear_clf.score(X_train, y_train))
	d={'accuracy':linear_clf.score(X_train, y_train)}
	return render(request,'acc1.html',d)

def mnb(request):
	from django.shortcuts import render
	from django.http import HttpResponse
	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	import itertools
	from sklearn import metrics
	import os
	import seaborn as sns
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import confusion_matrix
	df = pd.read_csv(r'C:\Users\sarka\Desktop\mini\Airpolution\pollution.csv')
	df1=df.fillna(0)
	from sklearn.preprocessing import LabelEncoder
	le = LabelEncoder()
	le
	dfle = df1.copy()
	dfle
	'''dfle.Name = le.fit_transform(dfle.Name)
	dfle.Location = le.fit_transform(dfle.Location)
	dfle.Fuel_Type = le.fit_transform(dfle.Fuel_Type)'''
	dfle.wnd_dir = le.fit_transform(dfle.wnd_dir)
	SE = le.fit_transform([['SE']])
	#dfle.Mileage = le.fit_transform(dfle.Mileage)
	#dfle.Engine = le.fit_transform(dfle.Engine)
	dfle
	print(dfle)
	X = dfle[['dew','temp','press','wnd_dir','wnd_spd','snow','rain']].values
	X
	y = dfle[['pollution']]
	y
	atest=[[-16,-4,1020,SE,1.79,0,0]]
	#train_test separation
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
	from sklearn import linear_model
	linear_clf = linear_model.Ridge()
	linear_clf.fit(X_train, y_train)
	pred = linear_clf.predict(X_test)
	#pred1 = linear_clf.predict(atest)
	print(pred)
	#print(pred1)
	print(linear_clf.score(X_train, y_train))
	d={'accuracy':linear_clf.score(X_train, y_train)}
	return render(request,'acc1.html',d)

def graph(request):
	from django.shortcuts import render
	from django.http import HttpResponse
	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	from sklearn.model_selection import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	import itertools
	from sklearn import metrics
	import os
	import seaborn as sns
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import confusion_matrix
	df = pd.read_csv(r'C:\Users\sarka\Desktop\mini\Airpolution\pollution.csv')
	df1=df.fillna(0)
	from sklearn.preprocessing import LabelEncoder
	le = LabelEncoder()
	le
	dfle = df1.copy()
	dfle
	'''dfle.Name = le.fit_transform(dfle.Name)
	dfle.Location = le.fit_transform(dfle.Location)
	dfle.Fuel_Type = le.fit_transform(dfle.Fuel_Type)'''
	dfle.wnd_dir = le.fit_transform(dfle.wnd_dir)
	SE = le.fit_transform([['SE']])
	#dfle.Mileage = le.fit_transform(dfle.Mileage)
	#dfle.Engine = le.fit_transform(dfle.Engine)
	dfle
	print(dfle)
	X = dfle[['dew','temp','press','wnd_dir','wnd_spd','snow','rain']].values
	X
	y = dfle[['pollution']]
	y
	atest=[[-16,-4,1020,SE,1.79,0,0]]
	#train_test separation
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
	from sklearn.svm import SVR
	linear_clf = SVR(kernel='rbf')
	linear_clf.fit(X_train, y_train)
	pred = linear_clf.predict(X_test)
	#pred1 = linear_clf.predict(atest)
	print(pred)
	#print(pred1)
	print(linear_clf.score(X_train, y_train))
	d={'accuracy':linear_clf.score(X_train, y_train)}
	return render(request,'acc1.html',d)

def accuracy(request):
	return render(request,'index.html')