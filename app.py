from fastapi import FastAPI , Path, HTTPException,Query
from fastapi.responses import JSONResponse
from schemas.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERSION
from schemas.prediction_response import PredictionResponse

app=FastAPI()
        
@app.get('/')
def home():
    return {'message':'Welcome to Insurance prediction Api'}    

@app.get('/health')
def health_check():
    return {'message':'ok',
            'Version':MODEL_VERSION,
            'model_loaded':model is not None
            }


@app.post('/predict',response_model=PredictionResponse)
def predict(data:UserInput):

    user_input={
            'income_lpa':data.income_lpa,
            'occupation':data.occupation,
            'bmi':data.bmi,
            'age_group':data.age_group,
            'lifestyle_risk':data.lifestyle_risk,
            'city_tier':data.city_tier    
        }


    try:
        prediction=predict_output(user_input)
        return JSONResponse(status_code=200,content={'response':prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))



