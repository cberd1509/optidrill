from keras.models import load_model
from keras import optimizers
from keras.models import Model
from keras.models import model_from_json
from sklearn.externals import joblib
from keras.utils import np_utils
import numpy as np
import keras


def getStuckProb(FormationOHE,MinWeight,MaxWeight,Caudal,MDTope,MDBase):

    
    keras.backend.clear_session()

    jsonFile = open('static/models/model.json','r')
    loaded_model_json = jsonFile.read()
    jsonFile.close()

    model = model_from_json(loaded_model_json)
    model.load_weights('static/models/model.h5')

    model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

    FormationOHE = np.array(FormationOHE)

    Datos = np.array([MinWeight, MaxWeight, Caudal, MDTope, MDBase])
    Datos = np.concatenate((FormationOHE,Datos)) #Vector de entrada
    
    #Montaje del escalador
    Datos = np.array([Datos])

    scaler = joblib.load('static/models/scaler.save')
    Datos = scaler.transform(Datos) #Vector de entrada escalado

    DatosR = np.reshape(Datos,(1,21))

    StuckIndex = model.predict(DatosR)
   
    print(StuckIndex)
    return StuckIndex
