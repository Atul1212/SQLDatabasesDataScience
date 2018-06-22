#Connect to the database
%load_ext sql
%sql ibm_db_sa://dfp88984:ks2922nh0f15%40tpw@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB

#Store dataset in a table
import pandas
#read .csv file from City of Chicago website
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
%sql PERSIST chicago_socioeconomic_data

#Check to see if table creation is successful
%sql SELECT * FROM chicago_socioeconomic_data LIMIT 10;

# How many rows are in the data set?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

# How many community areas in Chicago have a hardship index greater than 50.0?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;

# What is the maximum value of hardship in this dataset?
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;

# Which community area has the highest hardship index? 
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index = 98.0;

# Which Chicago community areas have per-capita incomes greater than $60,000?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;

#Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.¶
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())

#As income increases, hardship decreases.