import ibm_db

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            
dsn_hostname = "dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net" 
dsn_port = "50000"                
dsn_protocol = "TCPIP"            
dsn_uid = "dfp88984"        
dsn_pwd = "ks2922nh0f15@tpw"       

#Create database connection
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected!")

except:
    print ("Unable to connect to database")

#Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
dropQuery = "drop table INSTRUCTOR"

#Now execute the drop statment
dropStmt = ibm_db.exec_immediate(conn, dropQuery)

#Construct the Create Table DDL statement 
createQuery = "create table INSTRUCTOR(id INTEGER PRIMARY KEY NOT NULL, fname VARCHAR(15), lname VARCHAR(15), city VARCHAR(15), ccode CHAR(2))"

#Execute create
createStmt = ibm_db.exec_immediate(conn, createQuery)

#Construct the insert statement
insertQuery = "insert into INSTRUCTOR values(1,'Rav','Ahuja','TORONTO','CA')"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, insertQuery)

#construct insert statement 2 that adds other 2 rows
insertQuery2 = "insert into INSTRUCTOR values(2,'Raul','Chong','Markham','CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"

#execute the insert
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)

#Construct the query that retrieves all rows from the INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#Execute the statement
selectStmt = ibm_db.exec_immediate(conn, selectQuery)

#Fetch the Dictionary (for the first row only)
ibm_db.fetch_both(selectStmt)

#Fetch the rest of the rows and print the ID and FNAME for those rows
while ibm_db.fetch_row(selectStmt) != False:
   print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))

#Construct an update query
updateQuery = "update INSTRUCTOR set CITY='MOOSETOWN' where fname='Rav'"

#Execute update query
updateStmt = ibm_db.exec_immediate(conn, updateQuery)

import pandas
import ibm_db_dbi

#connection for pandas
pconn = ibm_db_dbi.Connection(conn)

#query statement to retrieve all rows in INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#retrieve the query results into a pandas dataframe
pdf = pandas.read_sql(selectQuery, pconn)

#print just the LNAME for first row in the pandas data frame
pdf.LNAME[0]

pdf
pdf.shape
ibm_db.close(conn)