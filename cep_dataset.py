# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:03:32 2017

@author: cake
"""

import pandas as pd

def load_states():
    state_fields=["STATE_ID", "STATE", "ABBREVIATION"]
    return pd.read_csv("./data/states.csv",names=state_fields, 
                                  header=None)
    
def load_cities():
    city_fields=["CITY_ID", "CITY", "STATE_ID"]
    return pd.read_csv("./data/cities.csv",names=city_fields, header=None)   

def load_locations():
    df_list= []
    loc_fields=["CEP","ADDRESS","NEIGHBOURHOOD","CITY_ID","STATE_ID"]
    for n in range(1,6):
        filename = "./data/sp.cepaberto_parte_{n}.csv".format(n=n)
        df_list.append(
            pd.read_csv("./data/sp.cepaberto_parte_1.csv",names=loc_fields, 
                        header=None)
        )
    return pd.concat(df_list) 

def merge_data(df_states, df_cities, df_locations):
    temp = pd.merge(df_cities,df_states,on="STATE_ID",how="inner")
    return pd.merge(df_locations, temp, on=["CITY_ID","STATE_ID"], how="inner")

def load_data():
    df_states = load_states()    
    df_cities = load_cities()
    df_locations = load_locations()
    return merge_data(df_states, df_cities, df_locations)

df = load_data()
df_sample = df.sample(n=10000,replace=False,random_state=42)
df_sample["ID"] = range(0, len(df_sample))

def get_image(row):
    query = "{address}, {neighbourhood}, {city}, {state} - CEP {CEP}".format(
        address = row["ADDRESS"],
        neighbourhood = row["NEIGHBOURHOOD"],
        city = row["CITY"],
        state = row["ABBREVIATION"],
        CEP=row["CEP"]
    )
    retrieve_address(row["ID"],query,imsize=(800,800), headings=range(0,360,60))
    
df_sample.apply(get_image, axis=1)