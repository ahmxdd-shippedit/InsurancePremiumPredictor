import pickle 
import pandas as pd
from schema.user_input import userInput

#importing the model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
MODEL_VERSION = '1.0.3'

def predict_output(userInput : dict):
    input_df = pd.DataFrame([userInput])
    output = model.predict(input_df)[0]
    
    return output
    