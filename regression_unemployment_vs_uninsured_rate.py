import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "fantasy"
import numpy as np
import random
import scipy
import scipy.misc
import scipy.cluster
from pandas.io.json import json_normalize

unployment_dataframe = pd.read_excel('Un.xlsx')

unployment_dataframe['State'] = unployment_dataframe['State Abb.'].map(lambda x:x. split(',')[1])
unployment_dataframe.set_index('State', drop=True, append=False, inplace=True, verify_integrity=False)
State_total = unployment_dataframe.groupby('State').sum()
State_total.drop(['2008_(%)', '2009_(%)','2010_(%)','2011_(%)','2012_(%)','2013_(%)','2014_(%)','2015_(%)','2016_(%)','2017_(%)','2018_(%)'], axis=1,inplace= True )
State_total.drop(['Code'], axis=1,inplace= True)
for i in range(11):
    State_total[f'{2008+i}'] = State_total.iloc[0:,3*i+2] / State_total.iloc[0:,3*i]*100
State_total_percentages_only = State_total.iloc[0:, -11:]
State_total_percentages_only_flipped = State_total_percentages_only.transpose()
State_total_percentages_only_flipped = State_total_percentages_only_flipped.rename({'State': 'Years'}, axis=1)
State_total_percentages_only_flipped.index.names = ['Years']
State_total_percentages_only_flipped.plot(figsize=(16, 20))

# hc_converage_2008_2018 HAS NOT BEEN READ IN YET. THIS IS JUST PUSHING THE FILE UP FOR THE RECORD






