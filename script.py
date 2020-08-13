#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#from sklearn.neighbors import KNeighborsClassifier
from flask import Flask, request, jsonify, render_template

import joblib


app = Flask(__name__, template_folder = 'template')



  
@app.route('/')
def index():
    return render_template('input.html')


 

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 4) 
    print("array:",to_predict)
    model_name = 'C:\\Users\\Dikhsha\\FINAL YEAR PROJECT\\deployment\\Knn_model_place_balanced.pkl'
    loaded_model = joblib.load(model_name,'r') 
    result = loaded_model.predict(to_predict) 
    print(result)
    return result[0] 

@app.route('/', methods =['GET','POST'])

def result(): 
    if request.method == 'POST':
        to_predict_list = list(map(int, request.form.to_dict().values()))  # list of integers as input
        print("Working till result")

        result = ValuePredictor(to_predict_list)         

        print(result)
        if int(result)== 0: 
            prediction = 'You can fall victim to: ARSON'
        
        elif int(result)== 2: 
            prediction = 'You can fall victim to: BURGLARY/ROBBERY'
        elif int(result)== 1:
            prediction = 'You can fall victim to: ASSAULT'
        elif int(result)== 4: 
            prediction = 'You can fall victim to: FRAUDS/THEFT-FRAUD'
        elif int(result)== 3: 
            prediction = 'You can fall victim to: CRIMINAL MISCHIEF/TRESPASS'
        elif int(result)== 5: 
            prediction = 'You can fall victim to: INTOXICATED & IMPAIRED DRIVING'
        elif int(result)== 6: 
            prediction = 'You can fall victim to: KIDNAPPING & RELATED OFFENSES'
        elif int(result)== 7: 
            prediction = 'You can fall victim to: LARCENY'
        elif int(result)== 8: 
            prediction = 'You can fall victim to: LARCENY/UNAUTHORISED USE OF MOTOR VEHICLE'
        elif int(result)== 9: 
            prediction = 'You can fall victim to: RAPE'
        elif int(result)== 10: 
            prediction = 'You can fall victim to: SEX CRIMES:HARRASSMENT,SEXUAL ASSAULT,PROSTITUTION'
        else: 
            prediction ='You can fall victim to: SEX CRIMES:RAPE,SEXUAL ASSAULT,PROSTITUTION'    

        return render_template("result.html", prediction = prediction)


if __name__ == '__main__':

    app.run(debug = True)





