%load_ext sql

# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
%sql ibm_db_sa://dfp88984:ks2922nh0f15%40tpw@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB

# Store the Chicago Socioeconomic Indicators dataset into a CENSUS_DATA table
CENSUSDATA = pandas.read_csv('https://ibm.box.com/shared/static/05c3415cbfbtfnr2fx4atenb2sd361ze.csv')
%sql PERSIST CENSUSDATA

# Store the Chicago Public Schools dataset into a CHICAGO_PUBLIC_SCHOOLS table
PUBLICSCHOOLS = pandas.read_csv('https://ibm.box.com/shared/static/0g7kbanvn5l2gt2qu38ukooatnjqyuys.csv')
%sql PERSIST PUBLICSCHOOLS

# Store the Chicago Crime Data dataset into a CHICAGO_CRIME_DATA table
CRIMEDATA = pandas.read_csv('https://ibm.box.com/shared/static/svflyugsr9zbqy5bmowgswqemfpm1x7f.csv')
%sql PERSIST CRIMEDATA

# Rows in Census Data (Socieconimic Indicators)
%sql SELECT COUNT(*) FROM CENSUSDATA;

# Rows in Public Schools
%sql SELECT COUNT(*) from PUBLICSCHOOLS;

# Rows in Crime Data
%sql SELECT COUNT(*) from CRIMEDATA;

# Find average college enrollments by community area

%%sql

SELECT "CommunityAreaName", AVG("CollegeEnrollmentNumberOfStudents") AS AVGCOLLEGE 
	FROM PUBLICSCHOOLS 
	GROUP BY "CommunityAreaName"

# Find number of schools that are health certified

%sql SELECT COUNT(*) FROM CHICAGO_PUBLIC_SCHOOLS WHERE "Healthy Schools Certified?" = 'Yes'

# How many observations have a location description of Gas Station

%sql SELECT COUNT(*) FROM CHICAGO_CRIME_DATA WHERE "Location Description" = 'GAS STATION'

# Retrieve a list of the top 10 community areas which have most number of schools and sorted in descending order.

%%sql

SELECT "CommunityAreaName", COUNT("CommunityAreaName") AS "num_schools" 
    FROM     PUBLICSCHOOLS
    GROUP BY "CommunityAreaName"
    ORDER BY "num_schools" DESC
    LIMIT    10;

# How many observations have value MOTOR VEHICLE THEFT in the Primary Type variable (this is the number of crimes related to Motor vehicles)

%sql SELECT COUNT(*) FROM CHICAGO_CRIME_DATA WHERE "Primary Type" = 'MOTOR VEHICLE THEFT'

# Find the minimum “Average Student Attendance” for community are where hardship is 96. 

%%sql 
SELECT MIN("AverageStudentAttendance")
	FROM PUBLICSCHOOLS
	INNER JOIN CENSUSDATA ON PUBLICSCHOOLS."CommunityAreaNumber" = CENSUSDATA."CommunityAreaNumber"
	WHERE "HardshipIndex" = 96;
