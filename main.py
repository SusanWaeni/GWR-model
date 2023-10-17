# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:22:10 2023

@author: BRYAN ASEGA
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Cross origin resource sharing
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware( # for the UI
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True
    allow_methods = ["*"]
    allow_headers = ["*"]
    )

class model_input(BaseModel): # user inputs
    T_depth : float
    WRL/SWL : float
    Drawdown(m) : float
    Yield (M3) : float
    Transmissivity : float
    Precipitation (MM/YR) : float
    
    
# load the saved model
GWR_model = pickle.load(open('Potential_GWR_model.sav', 'rb'))

@app.post('/Groundwater_recharge_prediction')
def gw_recharge_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    Depth = input_dictionary['T_depth']
    WS = input_dictionary['WRL/SWL']
    Drawd = input_dictionary['Drawdown(m)']
    Yield = input_dictionary['Yield (M3)']
    Transm = input_dictionary['Transmissivity']
    Precip = input_dictionary['Precipitation (MM/YR)']
    
    input_list = [Depth, WS, Drawd, Yield, Transm, Precip]
    
    prediction = GWR_model.predict([input_list])
    
    if prediction_label[0] == 0:
        return 'Poor Groundwater Recharge Area'
    else:
        return 'Potential Groundwater Recharge Area'










