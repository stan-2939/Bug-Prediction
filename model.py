from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

loaded_model = pickle.load(open("D:/Allianz/Project1/env/trained_model2.sav",'rb'))

def predict(attribute:np.array):
    pred=loaded_model.predict(attribute)
    return pred[0]

