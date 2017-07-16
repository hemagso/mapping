from keras.preprocessing.image import load_img
from sklearn.model_selection import train_test_split
from skimage.color import rgb2hsv
from math import ceil

import os
import numpy as np
import pandas as pd
import geopandas as gpd


def get_dataframe():
    df_coord = pd.read_csv("./data/coordinates_check_512.csv", names=["COD_SETOR","ID", "LAT", "LNG", "HAS_PICTURE"])
    df_geo = gpd.read_file("./data/income_map/income_map.shp")
    df_geo["COD_SETOR"] = pd.to_numeric(df_geo["COD_SETOR"],downcast="integer")

    df_coord.set_index("COD_SETOR", inplace=True)
    df_geo.set_index("COD_SETOR", inplace=True)
    df_final = df_coord.join(
        df_geo["LOG_MEAN_I"],
        how="inner"
    )
    return df_final

def get_image(sector, iid, colorspace="rgb"):    
    fullpath = "./images/streetview512/{sector:15d}/IMG_{sector:015d}_{iid:03d}.jpg".format(sector=int(sector), iid=int(iid))
    image = load_img(fullpath, target_size=(512,512))
    if colorspace == "rgb":
        return image
    elif colorspace == "hsv":
        return rgb2hsv(image)
    else:
        raise TypeError("Invalid color mode. Valid values are rgb or hsv")
        

def get_image_batch(batch_ids, colorspace="rgb"):
    nrows = batch_ids.shape[0]
    features = np.zeros((nrows, 512, 512,3))
    
    for idx, row in enumerate(batch_ids.iterrows()):
        sector, data = row
        iid = data["ID"]
        try:
            features[idx,:,:,:] = get_image(sector, iid, colorspace=colorspace)
        except ValueError as e:
            print(sector, iid)
        
    labels = batch_ids["LOG_MEAN_I"].values
    features = (features/255) - 0.5
    return features, labels
        

def batch_generator(df, batch_size=10000, shuffle=True, colorspace="rgb"):
    #Shuffling the dataframe
    if shuffle:
        df_int = df.sample(frac=1)
    else:
        df_int = df
        
    batch = 0
    end = batch_size
    while 1:
        start = batch*batch_size
        end = start + batch_size
        current = df_int[start:end]
        yield get_image_batch(current, colorspace=colorspace)
        batch = batch + 1  
        if end > df_int.shape[0]:
            batch = 1

def get_generators(df, batch_size=10, colorspace="rgb"):            
    df_temp, df_validate = train_test_split(df, test_size=0.1, random_state=42)
    df_train, df_test = train_test_split(df_temp, test_size=0.2/0.9, random_state=42)

    gen_train = batch_generator(df_train, batch_size=batch_size, colorspace=colorspace)
    gen_validate = batch_generator(df_validate, batch_size=batch_size, colorspace=colorspace)
    gen_test = batch_generator(df_test, batch_size=batch_size, colorspace=colorspace)    
        
    steps_train = ceil(df_train.shape[0]/batch_size)
    steps_validate = ceil(df_validate.shape[0]/batch_size)
    steps_test = ceil(df_test.shape[0]/batch_size)
        
    return {"data" : gen_train, "steps" : steps_train} , \
           {"data" : gen_validate, "steps" : steps_validate}, \
           {"data" : gen_test, "steps" : steps_test}