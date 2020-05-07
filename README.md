## Programming Analytics Final Project: Proposal and Data Exploration
### Team Members:
* Yuttawee Kongtananan (GitHub ID: yuttk)
* Vel (Tien-Yun) Wu (GitHub ID: velwu)
* Eva (Yi-Ting) Huang (GitHub ID: iameva62948)


### Data of interest
* Insurance Coverage.

* Spending per Household.

* Expenses paid for by insurance companies for their customers.

Source of Data: HIC-4. Health Insurance Coverage Status and Type of Coverage by State--All Persons: 2008 to 2018. Can be downloaded from: https://www.census.gov/library/publications/2019/demo/p60-267.html#

Healthcare coverage
https://www.census.gov/library/publications/2019/demo/p60-267.html#

National Center for Health Statistics
https://cdc.gov/nchs/nhis/nhis_2017_data_release.htm?fbclid=IwAR2s1_ur8ElTtcGjPHKl1zN7D0slSoTbLggHBFRR8X-awwF_YLCJIgvn_4Q

Us Census Bureau:Income Data Tables
https://www.census.gov/topics/income-poverty/income/data/tables.html

Consumer Price Index
https://www.bls.gov/cpi/



Some news: https://www.vox.com/policy-and-politics/2019/9/10/20858938/health-insurance-census-bureau-data-trump?fbclid=IwAR2s1_ur8ElTtcGjPHKl1zN7D0slSoTbLggHBFRR8X-awwF_YLCJIgvn_4Q

Some other sources: https://www.cdc.gov/nchs/nhis/nhis_2017_data_release.htm?fbclid=IwAR2s1_ur8ElTtcGjPHKl1zN7D0slSoTbLggHBFRR8X-awwF_YLCJIgvn_4Q

## Files: Py and Ipynb
### 1. central_analysis.py
- This is the main file. Everything what our project does programmatically is done here. Codes here are built on those originated from **2.** and **3.** below. Most are, suffice to say, overhauled to the point where parameters are no longer hard-coded, but instead follow the general object-oriented programming structure.

### 2. data_exploration.ipynb & data_exploration_2.ipynb
- There are multiple files of these names but they are more like test spaces where we try out codes to look at the datasets before putting functional codes into "central_analysis.py". Specifically, "data_exploration_2.ipynb" is built on "data_exploration.ipynb" with more visualization though parameters and data passages are still mostly hard-coded.

### 3. Household_Income.ipynb & Household_Income2.ipynb
- Household incomes are read and parsed in ways that allow them to return an uniform data structure which can be passed into different functions to create different visualizations. 

### 4. presentation_caller.ipynb
- This is the file we mainly use for demonstrations. It imports several popular libraries plus "central_analysis.py" as dependencies. Viewers of our codes may also run this file to observe the datasets in a comprehensive, interactive way.


IS 590 PR - Progr Analytics & Data Process Final Project Proposal (Type II)
Researh Question:
How does Unemployment Rate impact Insurance Coverage Ratio in different regions within the United States?

Attached to this proposal is a Data Exploration done using Jupyter Notebook, accessible through this link to our GitHub Repository:
https://github.com/velwu/employment_and_insurance_project

Hypotheses:
The Unemployment Rate negatively impacts the Insurance Coverage Ratio.
The effects of unemployment rate on insurance coverage ratio are not equal
The effects of unemployment rate on each type of insurance are not equal
There is a positive linear relationship between local unemployment rate and Direct-purchase insurance ratio
There is a positive linear correlation between the local unemployment rate and the uninsured ratio in each state
(Building on Hypothesis 5) There is no significant discrepancy between said correlations found in different states
(Building on Hypothesis 5) Within in each state, Direct-purchase Insurance Rates are affected more by Unemployment Rates for Large Metropolitan Areas than they are by Unemployment Rates for the entire state
		 	 	 					
I. Project Objective:
Contrary to countries like Japan, Taiwan and many in Europe, The United States does not have all its social / health insurance systems run by the central government. Instead, most citizens are financially responsible for the costs and responsibilities of their health insurance. In most cases, the primary health insurance coverage for an American resident comes in limited capacity through: (1) Publicly operated Medicaid / Medicare, (2) Private insurance companies and (3) Financially capable employers. Uninsured people not included in plans above must bear all medical and treatment expenses themselves. 
This project aims to address the relationship between Unemployment and Insurance Coverage within the United States. By analyzing data describing medical insurances, unemployment rates, and demographics in each state, we embark on a journey to investigate how much unemployment rates affect insurance coverage ratios and the shares of each insurance type in various regions.


II. Datasets Description
Datasets and other variables we use will be collected from sources such as U.S. CENSUS BUREAU and U.S. BUREAU OF LABOR STATISTICS, both of which serve as primary subjects of this project.
a. Local Area Unemployment Statistics
https://www.bls.gov/lau/lastrk19.htm 
Dataset description: This website includes data describing monthly and annual employment, unemployment, and labor force traits within Census regions, divisions, States, counties, cities, metropolitan areas, and residences / settlements of other forms. In the analysis, we will select some variables from the data as independent variables in terms of demographics and economy.			
b. Health Insurance Coverage Status and Type of Coverage by State--All Persons:2008 to 2018
https://www.census.gov/library/publications/2019/demo/p60-267.html# 
Dataset description: This report presents statistics on health insurance coverage in the United States from 2008 to 2018. The dataset also contains different insurance categories as  dependent variables.
Public Coverage:
•  Employment-based: Plan provided by an employer or union
• Direct-purchase: Coverage purchased directly from an insurance company or through a federal or state marketplace (e.g., healthcare. Gov).
• TRICARE: Coverage through TRICARE, formerly known as the Civilian Health and Medical Program of the Uniformed Services.

Private Coverage:
 • Medicare: Federal program which compensates healthcare costs for people of or over the age of 65, plus those under 65 but with long-term disabilities.
• Medicaid: Medicaid, the Children’s Health Insurance Program (CHIP), and individual state health plans.
• CHAMPVA or VA: Civilian Health and Medical Program of the Department of Veterans Affairs, as well as care provided by the Department of Veterans Affairs and the military

