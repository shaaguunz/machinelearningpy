import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import SnowballStemmer
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split


from flask import Flask,render_template,url_for,request
import pickle

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    df =pd.read_csv('spam.csv',encoding='latin-1')
    df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis =1,inplace=True)
    df.columns=['category','text']
    stemmer = SnowballStemmer('english')
    def clean_text(df):
        df = df.translate(str.maketrans('','',string.punctuation))
        words = [stemmer.stem(word) for word in df.split() if word.lower() not in stopwords.words('english')]
        return ' '.join(words)
    df['text'] = df['text'].apply(clean_text) # passsing values to functions one by one
    
    #converting data into a form that machine learning algorithm can make sense of 
    #using COunt vectorizer
    
    cv =CountVectorizer(encoding = "latin-1", strip_accents = "unicode", stop_words = "english")
    features = cv.fit_transform(df['text'])
    
    X_train, X_test, y_train, y_test = train_test_split(features, df['category'], test_size=0.33)
    #naive bayes classifier
    Multinb = MultinomialNB()
    Multinb.fit(X_train,y_train)
    Multinb.score(X_test,y_test)
    from sklearn.externals import joblib
    
    joblib.dump(Multinb, 'NB_spam_model.pkl')
    NB_spam_model = open('NB_spam_model.pkl','rb')
    Multinb= joblib.load(NB_spam_model)
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = Multinb.predict(vect)
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(app.run(debug=True, use_reloader=False))
    
    
    
   
    
    
    