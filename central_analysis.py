
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

df = pd.read_excel('Un.xlsx')
#Data Cleaning
df['State'] = df['State Abb.'].map(lambda x:x. split(',')[1])
df.set_index('State', drop=True, append=False, inplace=True, verify_integrity=False)
State_total = df.groupby('State').sum()
State_total.drop(['2008_(%)', '2009_(%)','2010_(%)','2011_(%)','2012_(%)','2013_(%)','2014_(%)','2015_(%)','2016_(%)','2017_(%)','2018_(%)'], axis=1,inplace= True )
State_total.drop(['Code'], axis=1,inplace= True)

# Find State_total['20XX_Percentage'] = State_total["20XX_Unemployed"] / State_total["20XX_Labor"]*100
for i in range(11):
    State_total[f'{2008+i}'] = State_total.iloc[0:,3*i+2] / State_total.iloc[0:,3*i]*100
State_total_percentages_only = State_total.iloc[0:, -11:]
# The same table, but flipped around
State_total_percentages_only_flipped = State_total_percentages_only.transpose()
State_total_percentages_only_flipped = State_total_percentages_only_flipped.rename({'State': 'Years'}, axis=1)
State_total_percentages_only_flipped.index.names = ['Years']
State_total_percentages_only_flipped.plot(figsize=(16, 20))
plt.show()

### PART 2: hc_coverage |  To-be-converted to .py
"""
# Read in the data and drop Excel sheet comment blocks
hc_converage_2008_2018 = pd.read_excel('hic04_acs.xls', skiprows = [0, 1, 2]).dropna(thresh = 2)

# Prepare the headers by year and sub-section
years = list(range(2018, 2007, -1))

each_year_sub = ['Estimate_number', 'Margin_of_Error_number', 'Percentage', 'Margin_of_Error_percentage']

headers_for_hc_coverage_census = ['Nation/State', 'Coverage Type']

for each in years:
    for each_sub in each_year_sub:
        headers_for_hc_coverage_census.append(str(each) + '_' + each_sub)

# Assign headers to data
hc_converage_2008_2018.columns = headers_for_hc_coverage_census
hc_converage_2008_2018 = hc_converage_2008_2018[hc_converage_2008_2018['Coverage Type'].notna()].ffill(axis=0)
hc_converage_2008_2018

#%%

hc_converage_2008_2018_estimate_percentages_only = hc_converage_2008_2018.iloc[0:, [0, 1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44]]

# Inspect only the "Uninsured" percentage, including a nationwide one
hc_uninsured_perc = hc_converage_2008_2018_estimate_percentages_only[hc_converage_2008_2018_estimate_percentages_only['Coverage Type'] == 'Uninsured']
hc_uninsured_perc = hc_uninsured_perc.drop(['Coverage Type'], axis = 1).reset_index().drop(['index'], axis = 1).replace("N", np.nan).bfill(axis=1).astype(
    {'2018_Percentage': 'float64',
     '2017_Percentage': 'float64',
     '2016_Percentage': 'float64',
     '2015_Percentage': 'float64',
     '2014_Percentage': 'float64',
     '2013_Percentage': 'float64',
     '2012_Percentage': 'float64',
     '2011_Percentage': 'float64',
     '2010_Percentage': 'float64',
     '2009_Percentage': 'float64',
     '2008_Percentage': 'float64'
    })
hc_uninsured_perc

#%%


# The same table, but flipped around

hc_uninsured_perc_flipped = hc_uninsured_perc.transpose().reset_index()
hc_uninsured_perc_flipped.columns = hc_uninsured_perc_flipped.iloc[0]
hc_uninsured_perc_flipped = hc_uninsured_perc_flipped.rename({'Nation/State': 'Years'}, axis=1)
hc_uninsured_perc_flipped = hc_uninsured_perc_flipped[1:].iloc[::-1].reset_index().drop(['index'], axis = 1)
hc_uninsured_perc_flipped['Years'] = hc_uninsured_perc_flipped['Years'].str.rstrip('egatnecreP_').astype({'Years': 'int'})
hc_uninsured_perc_flipped

#%%

plt.figure(figsize=(24,13))
plt.plot( 'Years', 'UNITED STATES', data=hc_uninsured_perc_flipped, marker='*', color='#4832a8', linewidth=5)
for each_state in hc_uninsured_perc_flipped.columns[2:]:
    plt.plot( 'Years', each_state, data=hc_uninsured_perc_flipped, marker='p', markersize=2, color=(random.random(), random.random(), random.random()), linewidth=1)
plt.legend()
plt.xlabel('Years', fontsize = 'xx-large')
plt.ylabel('Percentage of Uninsured People', fontsize = 'xx-large')


"""

# PART 3: Merging dataframes and obtain correlations |  To-be-converted to .py
"""
# State-wise unemployment rates
unemployment_perc_mergeable = State_total_percentages_only_flipped.reset_index().astype({'Years': 'int32'}).add_suffix('_unemployment')
# State-wise uninsured rates
# Also converting all state names to their abbreviated forms for convenience
# Conversion standard referenced from: https://gist.github.com/mshafrir/2646763
hc_uninsured_perc_mergeable = hc_uninsured_perc_flipped.rename(columns={
    "UNITED STATES": "USA",
    "ALABAMA": "AL",
    "ALASKA": "AK",
    "ARIZONA": "AZ",
    "ARKANSAS": "AR",
    "CALIFORNIA": "CA",
    "COLORADO": "CO",
    "CONNECTICUT": "CT",
    "DELAWARE": "DE",
    "DISTRICT OF COLUMBIA": "DC",
    "FLORIDA": "FL",
    "GEORGIA": "GA",
    "GU": "Guam",
    "HAWAII": "HI",
    "IDAHO": "ID",
    "ILLINOIS": "IL",
    "INDIANA": "IN",
    "IOWA": "IA",
    "KANSAS": "KS",
    "KENTUCKY": "KY",
    "LOUISIANA": "LA",
    "MAINE": "ME",
    "MARYLAND": "MD",
    "MASSACHUSETTS": "MA",
    "MICHIGAN": "MI",
    "MINNESOTA": "MN",
    "MISSISSIPPI": "MS",
    "MISSOURI": "MO",
    "MONTANA": "MT",
    "NEBRASKA": "NE",
    "NEVADA": "NV",
    "NEW HAMPSHIRE": "NH",
    "NEW JERSEY": "NJ",
    "NEW MEXICO": "NM",
    "NEW YORK": "NY",
    "NORTH CAROLINA": "NC",
    "NORTH DAKOTA": "ND",
    "OHIO": "OH",
    "OKLAHOMA": "OK",
    "OREGON": "OR",
    "PENNSYLVANIA": "PA",
    "RHODE ISLAND": "RI",
    "SOUTH CAROLINA": "SC",
    "SOUTH DAKOTA": "SD",
    "TENNESSEE": "TN",
    "TEXAS": "TX",
    "UTAH": "UT",
    "VERMONT": "VT",
    "VIRGINIA": "VA",
    "WASHINGTON": "WA",
    "WEST VIRGINIA": "WV",
    "WISCONSIN": "WI",
    "WYOMING": "WY"}).add_suffix('_uninsured')

# Merged dataframe with suffixes to differentiate
unem_unin_merged = pd.merge(hc_uninsured_perc_mergeable, unemployment_perc_mergeable, left_on='Years_uninsured', right_on='Years_unemployment').drop(['Years_unemployment'], axis = 1)
unem_unin_merged = unem_unin_merged.rename(columns={"Years_uninsured" : "Years"})
unem_unin_merged

#%%

#for each_column in unem_unin_merged:
#    print(each_column)

# Lists out columns that describe uninsurted percentages. The first one is nationwide (USA_uninsured) and so it is temporarily removed through slicing
uninsured_cols = [col for col in unem_unin_merged.columns if 'uninsured' in col]
unemployment_cols = [col for col in unem_unin_merged.columns if 'unemployment' in col]

# First, convers uninsured rates into float64 so correlations can be drawn
for each in uninsured_cols:
    unem_unin_merged = unem_unin_merged.astype({each: 'float64'})

# Then, iterates through each states where uninsured rate and unemployment columns match. Prints outs the correlation value
for each_uni in uninsured_cols[1:]:
    for each_une in unemployment_cols:
        if each_uni[0:2] == each_une[1:3]:
            print(each_uni[0:2], "Correlation:", unem_unin_merged[each_uni].corr(unem_unin_merged[each_une]))


"""



