import ibm_db

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            
dsn_hostname = "dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net"
dsn_port = "50000"                
dsn_protocol = "TCPIP"           
dsn_uid = "dfp88984"        
dsn_pwd = "ks2922nh0f15@tpw"       

#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)

#Create database connection

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected!")

except:
    print ("Unable to connect to database")

ibm_db.close(conn)