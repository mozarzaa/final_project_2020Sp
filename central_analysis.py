
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


states_and_their_abbreviations = {
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
        "D.C." :"DC",
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
        "WYOMING": "WY",
        "YEARS" :"Years"}


def read_unemployment_by_year(start_year: int, end_year: int) -> pd.DataFrame:
    """
    :param start_year: The first year of the dataframe read in from the Unemployment Data 'Un.xlsx'. No data exists before year 2008, so this number should be 2008 at minimum.
    :param end_year: The last year of the dataframe read in from the Unemployment Data 'Un.xlsx'. No data exists beyond year 2018, so this number should be 2018 at maximum.
    :return: State_total_percentages_only_flipped. This is a pandas dataframe containing only total unemployment percentages in all states.
    """

    if start_year < 2008 or end_year > 2018 or end_year < start_year:
        print("Botched year formats!! Check input values!")
        return None

    df = pd.read_excel('Un.xlsx')
    # Data Cleaning
    df['State'] = df['State Abb.'].map(lambda x: x.split(',')[1])
    df.set_index('State', drop=True, append=False, inplace=True, verify_integrity=False)
    State_total = df.groupby('State').sum()
    percs_to_be_dropped = []

    thing = end_year - start_year + 1

    for i in range(thing):
        percs_to_be_dropped.append(str(start_year + i) + '_(%)')
    # percs_to_be_dropped = ['2008_(%)', '2009_(%)', '2010_(%)', '2011_(%)', etc.]
    State_total.drop(percs_to_be_dropped, axis=1, inplace=True)
    State_total.drop(['Code'], axis=1, inplace=True)

    # Find State_total['20XX_Percentage'] = State_total["20XX_Unemployed"] / State_total["20XX_Labor"]*100
    for i in range(end_year - start_year + 1):
        State_total[f'{start_year + i}'] = State_total.iloc[0:, 3 * i + 2] / State_total.iloc[0:, 3 * i] * 100
    State_total_percentages_only = State_total.iloc[0:, -(end_year - start_year + 1):]
    # The same table, but flipped around
    State_total_percentages_only_flipped = State_total_percentages_only.transpose()
    State_total_percentages_only_flipped = State_total_percentages_only_flipped.rename({'State': 'Years'}, axis=1)
    State_total_percentages_only_flipped.index.names = ['Years']
    State_total_percentages_only_flipped.plot(figsize=(32, 18))
    plt.show()

    unemployment_perc_mergeable = State_total_percentages_only_flipped.reset_index().astype({'Years': 'int32'})
    unemployment_perc_mergeable.columns = unemployment_perc_mergeable.columns.str.replace(' ', '')

    return unemployment_perc_mergeable

def read_health_care_coverage_by_year(start_year: int, end_year: int, coverage_type: str) -> pd.DataFrame:
    # This function is made for the HIC-4. Health Insurance Coverage Status and Type of Coverage by State--All Persons files
    # It should work on similar files as long as they are also downloaded from: https://www.census.gov/library/publications/2019/demo/p60-267.html
    """
    :param start_year: The first year where the output dataframe will have. Should be 2008 minimum.
    :param end_year: The last year where the output dataframe will have. Should be 2018 maximum.
    :param coverage_type: Can be 'Uninsured', 'Public', 'Private', '..Employer-based', '..VA Care' etc.
    :return: A dataframe which describes the insurance type's coverage in all states.
    """
    if start_year < 2008 or end_year > 2018 or end_year < start_year:
        print("Botched year formats!! Check input values!")
        return None

    hc_converage = pd.read_excel('hic04_acs.xls', skiprows=[0, 1, 2]).dropna(thresh=2)
    years = list(range(end_year, start_year-1, -1))

    each_year_sub = ['Estimate_number', 'Margin_of_Error_number', 'Percentage', 'Margin_of_Error_percentage']
    headers_for_hc_coverage_census = ['Nation/State', 'Coverage Type']

    for each in years:
        for each_sub in each_year_sub:
            headers_for_hc_coverage_census.append(str(each) + '_' + each_sub)

    # Subset the dataframe according to speicified year range, then assign headers to the subset
    hc_converage = hc_converage.iloc[:, 0: len(headers_for_hc_coverage_census)]
    hc_converage.columns = headers_for_hc_coverage_census
    hc_converage = hc_converage[hc_converage['Coverage Type'].notna()].ffill(axis=0)

    iloc_column_num_list = [0, 1]
    for i in range(end_year - start_year + 1):
        iloc_column_num_list.append((i+1)*4)

    # The original Excel file is
    hc_converage_estimate_percentages_only = hc_converage.iloc[0:, iloc_column_num_list]

    # Inspect only the "Uninsured" percentage, including a nationwide one
    hc_uninsured_perc = hc_converage_estimate_percentages_only[
        hc_converage_estimate_percentages_only['Coverage Type'] == coverage_type]

    casting_dict = {}
    for i in range(end_year, start_year - 1, -1):
        casting_dict.update({str(i) + '_Percentage': 'float64'})

    hc_uninsured_perc = hc_uninsured_perc.drop(['Coverage Type'], axis=1).reset_index().drop(['index'], axis=1).replace(
        "N", np.nan).bfill(axis=1).astype(casting_dict)

    hc_uninsured_perc_flipped = hc_uninsured_perc.transpose().reset_index()
    hc_uninsured_perc_flipped.columns = hc_uninsured_perc_flipped.iloc[0]
    hc_uninsured_perc_flipped = hc_uninsured_perc_flipped.rename({'Nation/State': 'Years'}, axis=1)
    hc_uninsured_perc_flipped = hc_uninsured_perc_flipped[1:].iloc[::-1].reset_index().drop(['index'], axis=1)
    hc_uninsured_perc_flipped['Years'] = hc_uninsured_perc_flipped['Years'].str.rstrip('egatnecreP_').astype(
        {'Years': 'int'})
    plt.figure(figsize=(24, 13))
    plt.plot('Years', 'UNITED STATES', data=hc_uninsured_perc_flipped, marker='*', color='#4832a8', linewidth=5)
    for each_state in hc_uninsured_perc_flipped.columns[2:]:
        plt.plot('Years', each_state, data=hc_uninsured_perc_flipped, marker='p', markersize=2,
                 color=(random.random(), random.random(), random.random()), linewidth=1)
    plt.legend()
    plt.xlabel('Years', fontsize='xx-large')
    plt.ylabel('Percentage of People: ' + coverage_type, fontsize='xx-large')
    plt.show()

    # Also converting all state names to their abbreviated forms for convenience
    # Conversion standard referenced from: https://gist.github.com/mshafrir/2646763
    hc_uninsured_perc_mergeable = hc_uninsured_perc_flipped.rename(columns=states_and_their_abbreviations)
    # Converts rates into float64 so correlations can be drawn
    for each in hc_uninsured_perc_mergeable.columns:
        if hc_uninsured_perc_mergeable[each].dtype == 'object':
            hc_uninsured_perc_mergeable = hc_uninsured_perc_mergeable.astype({each: 'float64'})

    # hc_uninsured_perc_mergeable = hc_uninsured_perc_mergeable.drop(['USA'], axis=1)
    return hc_uninsured_perc_mergeable

def read_household_income_by_year(start_year: int, end_year: int) -> pd.DataFrame:
    """
    :param start_year: The first year where the output dataframe will have. Should be 1984 minimum.
    :param end_year: The last year where the output dataframe will have. Should be 2018 maximum.
    :return: A dataframe recording household income in USD within each state, subsetted by the year range specified.
    """
    if start_year < 1984 or end_year > 2018 or end_year < start_year:
        print("Botched year formats!! Check input values!")
        return None

    df = pd.read_excel('Household Income.xls')
    df_flipped = df.transpose().reset_index()
    df_flipped.columns = df_flipped.iloc[0]
    df_flipped = df_flipped.rename({'States': 'Years'}, axis=1)
    df_flipped = df_flipped[1:].iloc[::-1].reset_index().drop(['index'], axis=1)
    df_flipped = df_flipped.astype({"Years": 'int32'})
    # Note to self: For Pandas, the "AND" condition is denoted by "&" not "and"
    df_flipped = df_flipped.loc[(df_flipped['Years'] >= start_year) & (df_flipped['Years'] <= end_year)]
    # For some reason, this dataframe's Years are sorted in descending order. It does not impede merging with other frames, but an ascending sort is left here just in case.
    # df_flipped = df_flipped.sort_values(by='Years', ascending=True)

    # Plotting
    plt.figure(figsize=(24, 13))
    plt.plot('Years', 'United States', data=df_flipped, marker='*', color='#4832a8', linewidth=5)
    for each_state in df_flipped.columns[2:]:
        plt.plot('Years', each_state, data=df_flipped, marker='p', markersize=2,
                 color=(random.random(), random.random(), random.random()), linewidth=1)
    plt.legend()
    plt.xlabel('Years', fontsize='xx-large')
    plt.ylabel('Household Income (USD)', fontsize='xx-large')
    plt.show()

    # Transforming the dataframe column names to adhere to the same format as other methods
    df_flipped.columns = df_flipped.columns.str.upper()
    df_flipped = df_flipped.rename(columns=states_and_their_abbreviations)

    # Type casting to make the dataframe returned more mergeable with others
    for each in df_flipped.columns:
        if df_flipped[each].dtype == 'object':
            df_flipped = df_flipped.astype({each: 'float64'})

    return df_flipped

def merging_dataframes_on_years_plus_correlations(dataframe_1: pd.DataFrame, dataframe_2: pd.DataFrame, suffix_1: str, suffix_2: str, compare_growth_rate: bool)-> pd.DataFrame:
    """
    :param dataframe_1: A pandas dataframe with a "Years" (int32) denoting years in the Solar Calendar format, and statistics (float64) for each state in U.S.A. using state codes (IL, TX, VA, etc.)
    :param dataframe_2: Another pandas dataframe with an exact same structure as dataframe_1.
    :param suffix_1: Suffixes to add to columns from dataframe_1.
    :param suffix_2: Suffixes to add to columns from dataframe_2.
    :param compare_growth_rate: This boolean value decides whether the correlation will be drawn between the percentage changes of values from both dataframes.
    Setting this to 'False' makes the program draw correlations over raw values, which might overestimate the correlations.
    :return: A merged dataframe with columns from both input dataframes. Because the join type is inner, only years which both dataframe contain will be left.
    """

    # Allocate the 2 dataframes to a location in memory with suffixes to differentiate their columns pointing to the same years
    dataframe_1 = dataframe_1.reset_index().add_suffix('_'  + suffix_1)
    dataframe_2 = dataframe_2.reset_index().add_suffix('_'  + suffix_2)

    dataframe_merged = pd.merge(dataframe_1, dataframe_2,  left_on = "Years" + '_'  + suffix_1, right_on = "Years" + '_'  + suffix_2, how='inner')

    # Lists out columns from both dataframes
    df1_cols = [col for col in dataframe_merged.columns if '_'  + suffix_1 in col and "Years" not in col and "index" not in col]
    df2_cols = [col for col in dataframe_merged.columns if '_'  + suffix_2 in col and "Years" not in col and "index" not in col]

    # Then, iterates through each states where columns of same states match. Prints outs the correlation value for each state
    if compare_growth_rate:
        print(suffix_1, "&", suffix_2, "Correlations w/ growth rates:")
    else:
        print(suffix_1, "&", suffix_2, "Correlations w/ raw values:")
    for each_df1_col in df1_cols:
        for each_df2_col in df2_cols:
            if each_df1_col[0:2] == each_df2_col[0:2]:
                if compare_growth_rate:
                    print(each_df1_col[0:2],
                          dataframe_merged.pct_change()[each_df1_col].corr(dataframe_merged.pct_change()[each_df2_col]))
                else:
                    print(each_df1_col[0:2], dataframe_merged[each_df1_col].corr(dataframe_merged[each_df2_col]))

    return dataframe_merged

def main_test():
    test_df_un = read_unemployment_by_year(2008, 2018)
    #print(test_df_un)
    #print(test_df_un.dtypes)

    test_df_hc = read_health_care_coverage_by_year(2008, 2017, 'Public')
    #print(test_df_hc)
    #print(test_df_hc.dtypes)

    test_df_hh_ic = read_household_income_by_year(1991, 2018)
    #print(test_df_hh_ic)

    test_df_merged = merging_dataframes_on_years_plus_correlations(test_df_un, test_df_hh_ic, "Unemployment", "HouseHold Income", False)
    # print(test_df_merged)
main_test()





