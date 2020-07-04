# ---
# jupyter:
#   jupytext:
#     formats: ipynb,../scripts/preparation//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd 
import numpy as np
import datasist as ds 
import matplotlib.pyplot as plt 
import seaborn as sns 
# %matplotlib inline 

import os 

os.getcwd()

os.chdir('C:\\Users\\HP\\Titanic\\Titanic\\data\\raw')

tit=pd.read_csv('titanic_train.csv')

ds.structdata.describe(tit)

#Display the misssing value from our dataset 
ds.structdata.display_missing(tit)

#separate label from data 
label=tit.Survived 
tit.drop(columns=['Survived','Name','PassengerId','Ticket','Cabin'],inplace=True, axis=1)

tit.head()

label

#Encode all categorical features
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()

for col in tit.columns:
    tit[col]=lb.fit_transform(tit[col])


