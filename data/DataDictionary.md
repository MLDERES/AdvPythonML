# Boston Housing
This dataset contains information collected by the US Census Service concerning housing in the area of Boston Massachusetts. It was obtained from the StatLib archive (http://lib.stat.cmu.edu/datasets/boston). The dataset has 506 cases.
Source: The data was originally published by Harrison, D. and Rubinfeld, D.L. `Hedonic prices and the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102, 1978.
There are 14 attributes in each case of the dataset. They are:
    
    CRIM 	per capita crime rate by town
    ZN     	proportion of residential land zoned for lots over 25,000 sq.ft.
    INDUS	proportion of non-retail business acres per town.
    CHAS 	Charles River dummy variable (1 if tract bounds river; 0 otherwise)
    NOX   	nitric oxides concentration (parts per 10 million)
    RM    	average number of rooms per dwelling
    AGE   	proportion of owner-occupied units built prior to 1940
    DIS   	weighted distances to five Boston employment centres
    RAD  	index of accessibility to radial highways
    TAX  	full-value property-tax rate per $10,000
    PTRATIO 	pupil-teacher ratio by town
    LSTAT   	% lower status of the population
    MEDV	Median value of owner-occupied homes in $1000

# Cereal
Source: DATA ANALYSIS FOR STUDENT LEARNING (DASL)

1. Name: Name of cereal
2. mfr: Manufacturer of cereal where A = American Home Food Products; G = General Mills; K = 
    Kelloggs; N = Nabisco; P = Post; Q = Quaker Oats; R = Ralston Purina
3. type: cold or hot
4. calories: calories per serving
5. protein: grams of protein
6. fat: grams of fat
7. sodium: milligrams of sodium
8. fiber: grams of dietary fiber
9. carbo: grams of complex carbohydrates
10. sugars: grams of sugars
11. potass: milligrams of potassium
12. vitamins: vitamins and minerals - 0, 25, or 100, indicating the typical percentage of FDA 
      recommended
13. shelf: display shelf (1, 2, or 3, counting from the floor)
14. weight: weight in ounces of one serving
15. cups: number of cups in one serving
16. rating: a rating of the cereals calculated by Consumer Reports

# GermanCredit
| Variable Name    | Description                                 | Variable Type | Code Description                                                 |
| :--------------- | :------------------------------------------ | :------------ | :--------------------------------------------------------------- |
| OBS#             | Observation No.                             | Categorical   |
| CHK_ACCT         | Checking account status                     | Categorical   | 0: < 0 DM                                                        |
|                  |                                             |               | 1:  0 < ...< 200 DM                                              |
|                  |                                             |               | 2: => 200 DM                                                     |
|                  |                                             |               | 3:  no checking account                                          |
| DURATION         | Duration of credit in months                | Numerical     |
| HISTORY          | Credit history                              | Categorical   | 0: no credits taken                                              |
|                  |                                             |               | 1: all credits at this bank paid back duly                       |
|                  |                                             |               | 2: existing credits paid back duly till now                      |
|                  |                                             |               | 3: delay in paying off in the past                               |
|                  |                                             |               | 4: critical account                                              |
| NEW_CAR          | Purpose of credit                           | Binary        | car (new) 0: No, 1: Yes                                          |
| USED_CAR         | Purpose of credit                           | Binary        | car (used) 0: No, 1: Yes                                         |
| FURNITURE        | Purpose of credit                           | Binary        | furniture/equipment 0: No, 1: Yes                                |
| RADIO/TV         | Purpose of credit                           | Binary        | radio/television 0: No, 1: Yes                                   |
| EDUCATION        | Purpose of credit                           | Binary        | education 0: No, 1: Yes                                          |
| RETRAINING       | Purpose of credit                           | Binary        | retraining 0: No, 1: Yes                                         |
| AMOUNT           | Credit amount                               | Numerical     |
| SAV_ACCT         | Average balance in savings account          | Categorical   | 0 : <  100 DM                                                    |
|                  |                                             |               | 1 : 100<= ... <  500 DM                                          |
|                  |                                             |               | 2 : 500<= ... < 1000 DM                                          |
|                  |                                             |               | 3 : =>1000 DM                                                    |
|                  |                                             |               | 4 : unknown/ no savings account                                  |
| EMPLOYMENT       | Present employment since                    | Categorical   | 0 : unemployed                                                   |
|                  |                                             |               | 1 :  < 1 year                                                    |
|                  |                                             |               | 2 : 1 <= ... < 4 years                                           |
|                  |                                             |               | 3 : 4 <=... < 7 years                                            |
|                  |                                             |               | 4 : >= 7 years                                                   |
| INSTALL_RATE     | Installment rate as % of disposable income  | Numerical     |
| MALE_DIV         | Applicant is male and divorced              | Binary        | 0: No, 1: Yes                                                    |
| MALE_SINGLE      | Applicant is male and single                | Binary        | 0: No, 1: Yes                                                    |
| MALE_MAR_WID     | Applicant is male and married or a widower  | Binary        | 0: No, 1: Yes                                                    |
| CO-APPLICANT     | Application has a co-applicant              | Binary        | 0: No, 1: Yes                                                    |
| GUARANTOR        | Applicant has a guarantor                   | Binary        | 0: No, 1: Yes                                                    |
| PRESENT_RESIDENT | Present resident since-years                | Categorical   | 0: <= 1 year                                                     |
|                  |                                             |               | 1<…<=2 years                                                     |
|                  |                                             |               | 2<…<=3 years                                                     |
|                  |                                             |               | 3:>4years                                                        |
| REAL_ESTATE      | Applicant owns real estate                  | Binary        | 0: No, 1: Yes                                                    |
| PROP_UNKN_NONE   | Applicant owns no property (or unknown)     | Binary        | 0: No, 1: Yes                                                    |
| AGE              | Age in years                                | Numerical     |
| OTHER_INSTALL    | Applicant has other installment plan credit | Binary        | 0: No, 1: Yes                                                    |
| RENT             | Applicant rents                             | Binary        | 0: No, 1: Yes                                                    |
| OWN_RES          | Applicant owns residence                    | Binary        | 0: No, 1: Yes                                                    |
| NUM_CREDITS      | Number of existing credits at this bank     | Numerical     |
| JOB              | Nature of job                               | Categorical   | 0: unemployed/ unskilled  - non-resident                         |
|                  |                                             |               | 1: unskilled - resident                                          |
|                  |                                             |               | 2: skilled employee / official                                   |
|                  |                                             |               | 3: management/ self-employed/highly  qualified employee/ officer |
NUM_DEPENDENTS  | Number of people for whom liable to provide maintenance |   Numerical|
TELEPHONE|        Applicant has phone in his or her name | Binary |   0: No, 1: Yes
FOREIGN |  	   Foreign worker   		     |    Binary     | 0: No, 1: Yes
RESPONSE|         Credit rating is good|   	         Binary  |    0: No, 1: Yes   	
