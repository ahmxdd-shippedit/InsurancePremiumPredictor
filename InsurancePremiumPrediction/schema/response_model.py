from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    prediction_category: str = Field(... , description='The predicted insurance premium')
    
    
    