import pickle
from fastapi import FastAPI
import uvicorn
import pandas as pd

from base import model

with open("classifer","rb") as file:

   loaded_model =  pickle.load(file)



app = FastAPI()
@app.get("/")
def hello_world():

    return {"message":"hello world"}

@app.post("/predict")
def predict_performance(data:model):
    
    data = data.dict()

    Age = data["Age"]
    Gender = data["Gender"]
    Ethnicity= data["Ethnicity"]
    ParentalEducation = data["ParentalEducation"]
    StudyTimeWeekly = data["StudyTimeWeekly"]
    Absences  =  data["Absences"]
    Tutoring  =  data["Tutoring"]
    ParentalSupport =  data["ParentalSupport"]
    Extracurricular =  data["Extracurricular"]
    Sports  =  data["Sports"]
    Music   = data["Music"]
    Volunteering  = data["Volunteering"] 


    predictions = loaded_model.predict([[Age,Gender,Ethnicity,ParentalEducation,StudyTimeWeekly,Absences,Tutoring,ParentalSupport,Extracurricular,
                           Sports,Music,Volunteering]])
    

    print("the predictions",predictions)

   
    if predictions[0]>3:

        return {"message":"Good Job","grade":predictions[0]}
    
    elif predictions[0] > 2 and predictions[0]<=3 :

        return {"message":"Alright,decent","grade":predictions[0]}
    
    else:

        return {"message":"Fair, you can do better","grade":predictions[0]}
