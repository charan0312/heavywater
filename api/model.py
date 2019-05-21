# -*- coding: utf-8 -*-

#import numpy as np
import pandas as pd
#import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
#from sklearn.metrics import log_loss, accuracy_score


df = pd.read_csv('shuffled-full-set-hashed.csv',names = ["label", "words"])

df.dropna(inplace=True)

X = df['words']
y = df['label']

y_ = pd.get_dummies(y)
y_.shape

seed = 10
validation_size = 0.20
X_train, X_test, y_train, y_test = train_test_split(X, y_, test_size=validation_size, random_state=seed)


vectorizer = TfidfVectorizer(max_features=10000)
X_train = vectorizer.fit_transform(X_train.values)
X_test = vectorizer.transform(X_test.values)

n_feat = 10000
def get_model(n_feat):
    model = Sequential()
    model.add(Dense(128, activation='relu', input_dim=n_feat))
    model.add(Dense(128, activation="sigmoid"))
    #model.add(Dropout(.2))
    #model.add(Dense(256, activation="sigmoid"))
    model.add(Dropout(.5))
    model.add(Dense(14, activation="softmax"))
    model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

NN = get_model(n_feat)
history = NN.fit(X_train,y_train, epochs=5, batch_size=64, validation_data=(X_test, y_test))

NN.save("nn_model.h5")
from sklearn.externals import joblib
joblib.dump(vectorizer, 'vec.pkl')
print("vectorizer dumped!")
