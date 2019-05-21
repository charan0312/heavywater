#import pandas as pd
import numpy as np

from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from sklearn.externals import joblib
#from sklearn.feature_extraction.text import TfidfVectorizer

# Your API definition
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/error/')
def error():
    return render_template('error.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        if loaded_model:
            try:
                doc = request.form['document']
                if doc.isspace():
                    return render_template('error.html')
                else:
                    comment = doc.split(':')
                      
                    #print(comment, len(comment))
                    l = []
                    
                    for i in range(len(comment)):
                        
                        padded_1 = vectorizer.transform([comment[i]])
            
                        pred_1 = loaded_model.predict(padded_1)
                        l.append([labels[np.argmax(pred_1)], max(pred_1[0])])
                        
               
                    return render_template('result.html',prediction = l)
    
            except:
    
                return render_template('error.html')
        else:
            print ('Train the model first')
            return ('No model here to use')
    
    
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 5000 

    loaded_model = load_model('nn_model.h5')
    vectorizer = joblib.load("vec.pkl") # Load "model_columns.pkl"
    labels = ['APPLICATION', 'BILL', 'BILL BINDER', 'BINDER', 'CANCELLATION NOTICE','CHANGE ENDORSEMENT', 'DECLARATION', 'DELETION OF INTEREST','EXPIRATION NOTICE', 'INTENT TO CANCEL NOTICE', 'NON-RENEWAL NOTICE','POLICY CHANGE', 'REINSTATEMENT NOTICE', 'RETURNED CHECK']

    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)