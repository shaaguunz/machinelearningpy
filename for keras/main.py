from keras.models import Sequential
from keras.layers import Dense
from pandas import read_csv

import numpy
seed =6
numpy.random.seed(seed)
filename = 'BBC.CSV'
dataframe - read_csv(filename)
array  = dataframe.values
X = array[:,0:11]  # array for data test
Y = array[:,11]
# building models
model = Sequential()
model.add(Dense(12,input_dim =11,init='uniform',activation = 'relu'))
model.add(Dense(8,init='uniform',activation = 'relu'))
model.add(Dense(8,init='uniform',activation = 'relu'))
model.add(Dense(8,init='uniform',activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam',metrics= ['accuracy'])
model.fit(X,Y,nb_epoch = 50,batch_size = 10)
scores = model.evaluate(X,Y)
print("%s : %.2f%" % (model.metrics_names[1],scores[1]*100))

