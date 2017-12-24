import pandas as pd
import numpy as np
ads=pd.read_csv("/users/hp/Desktop/IDS/HW1/ads_dataset.tsv",sep='\t')

def getDfSummary(input_data):
    output_data=input_data.describe()
    output_data=output_data.drop(["count","mean"])
    number_nan=[]
    number_distinct=[]
       
    for col in input_data.columns:
        number_nan.append(input_data[col].isnull().sum())
        number_distinct.append(input_data[col].nunique())
    output_data.loc["number_nan"]=number_nan
    output_data.loc["number_distinct"]=number_distinct
    return output_data

output1=getDfSummary(ads)



