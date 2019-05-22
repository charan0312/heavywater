import traceback, json
#import pandas as pd
import numpy as np

from flask import Flask, request, jsonify
from keras.models import load_model
from sklearn.externals import joblib
#from sklearn.feature_extraction.text import TfidfVectorizer

# Your API definition
app = Flask(__name__)


@app.route('/')
def home():
    return "Hi this is a document classification api"

@app.route('/predict', methods=['POST'])
def predict():
    if loaded_model:
        try:

            doc = request.args.get('words')
            padded_1 = vectorizer.transform([doc])
            l = []
            pred_1 = loaded_model.predict(padded_1)
            l.append({'prediction': str(labels[np.argmax(pred_1)]), 'confidence': str(max(pred_1[0]))})
            
            

            return jsonify(l)
            
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
    
    
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 8080 

    
    loaded_model = load_model('nn_model.h5')
#    print ('Model loaded')
    vectorizer = joblib.load("vec.pkl") # Load "model_columns.pkl"

    labels = ['APPLICATION', 'BILL', 'BILL BINDER', 'BINDER', 'CANCELLATION NOTICE','CHANGE ENDORSEMENT', 'DECLARATION', 'DELETION OF INTEREST','EXPIRATION NOTICE', 'INTENT TO CANCEL NOTICE', 'NON-RENEWAL NOTICE','POLICY CHANGE', 'REINSTATEMENT NOTICE', 'RETURNED CHECK']

    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
