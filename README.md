## Programming Analytics Final Project: Proposal and Data Exploration
### Team Members:
* Yuttawee Kongtananan (GitHub ID: yuttk)
* Vel (Tien-Yun) Wu (GitHub ID: velwu)
* Eva (Yi-Ting) Huang (GitHub ID: iameva62948)

###Data of interest
* Insurance Coverage.

* Spending per Household.

* Expenses paid for by insurance companies for their customers.

Source of Data: HIC-4. Health Insurance Coverage Status and Type of Coverage by State--All Persons: 2008 to 2018. Can be downloaded from: https://www.census.gov/library/publications/2019/demo/p60-267.html#

Some news: https://www.vox.com/policy-and-politics/2019/9/10/20858938/health-insurance-census-bureau-data-trump?fbclid=IwAR2s1_ur8ElTtcGjPHKl1zN7D0slSoTbLggHBFRR8X-awwF_YLCJIgvn_4Q

Some other sources: https://www.cdc.gov/nchs/nhis/nhis_2017_data_release.htm?fbclid=IwAR2s1_ur8ElTtcGjPHKl1zN7D0slSoTbLggHBFRR8X-awwF_YLCJIgvn_4Q

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

III. Proposed Analysis	

We plan to generate different linear regression models based on the unemployment rate and regional characteristics over the years. Furthermore, we want to see how the unemployment rate affects the shares of each insurance type. We will choose the best linear regression with the smallest RMSE. Overall, it will help us and the government analyze whether the unemployment rate and the insurance ratio are highly correlated, because the news "The uninsured rate had been steadily declining for a decade. But now it is rising again." mentioned "The increase in the number of "Uninsured is surprising because the US economy has been relatively strong and unemployment has remained low.", but no relevant data details are provided. Therefore, this analysis can give support or refute for this news.

News source: https://www.vox.com/policy-and-politics/2019/9/10/20858938/health-insurance-census-bureau-data-trump?fbclid=IwAR2s1_ur8ElTtcGjPHKl1zN7D0slSoTbLggHBFRR8X-awwF_YLCJIgvn
