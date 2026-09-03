from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output, MODEL_VERSION
from schema.user_input import userInput
    
app = FastAPI()
        
@app.get('/')
def home():
    return {
        'message' : 'Insurance Premium Predictor'
    }

@app.get('/health')
def health_check():
    return {
        'status' : 'ok',
        'Model Version' : 'MODEL_VERSION'
    }
    
@app.post('/predict')
def predict_premium(data : userInput):
    
    user_input = {
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
        'bmi': data.bmi,
        'Age Group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city tier': data.city_tier,
    }
    
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category' : prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))                                         