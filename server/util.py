import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqm,bath,room):
    try:
        loc_index = __data_columns.index(location.lower())
        

    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))

    x[0] = sqm
    x[1] = room
    x[2] = bath

    if loc_index>=0:
        x[loc_index] = 1


    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqm, bath, room

    global __model
    if __model is None:
        with open('./artifacts/Tunisia_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('bizerte',100,1,2))
    print(get_estimated_price('tunis', 90, 2, 4))
    print(get_estimated_price('Monastir', 150, 1, 2)) 
    print(get_estimated_price('Sousse', 120, 2, 2)) 