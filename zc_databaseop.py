"""
 This tutorial would cover connecting to MySQL database. Connection to a database is done with connectors.
 Every database (e.g. SQLServer, OracleDB, MongoDB, CosmoDB, PostgreSQL, MySQL) all have their own 
 connectors

        Python App ===========MySQL Connector==========>MySQL Database

Steps to Working with MySQL DB
    1. Install MySQL connector
    2. import the connector
    3. Use connector to CREATE CONNECTION TO DB
    4. Use connection to CREATE A CURSOR (This is used to perform CRUD operations)
    5. CREATE A TABLE

Tips: You can install a GUI tool to work with MySQL such as MySQL workbench
Note: Make sure you provide a ROOT password when installing MySQL

Insalling MySQL Connector: pip install mysql-connector-python

Creating a database and table for storing data:
    create databased eradicatordb
    use eradicatordb
    create table userinfo(id int, firstname varchar(20), lastname varchar(20), 
                          salary int, department varchar(30))

Selecting Table: select * from userinfo

Connecting from the DB from your python app:
    import mysql.connector

    #MySQL Default Port is 3306
    try:
        conn = mysql.connector.connect(host='localhost',database='eradicatordb', 
                                    user='root',password='mypassword')

    except:
        print("Connection failed, Please check your parameters and try again")

    else:
        print("Connected to DB")

    finally:
        pass

Note: You can use conn.is_connected() which returns a boolean to check if connection succeeded or not.
        Also make sure the connection to the DB is closed after execution is done. Run conn.close() to
        close the connection to the database.

Performing CRUD Operations:
    As earlier stated, CRUD operations are implemented using a CURSOR object.

 ##READING FROM DB
    cusor = conn.cursor()

    #cursor.execute("<SQL Statement goes here>")
    cursor.execute("select * from userinfo")

    #Return one row at a time from the cursor execution
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
    cursor.close()

    #Return all row of the cursor execution
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

    #Printing the Total numbers of row in the DB can be done via:
    cursor.rowcount

    ##CREATING RECORD (INSERTING) IN DB
    cusor = conn.cursor()

    try:
        cursor.execute("insert into userinfo values (1,'Ifere','Okibe', 500,'Operations')")
        conn.commit()
    execpt:
        conn.rollback()
    else:
        print("User Information Added Successful")
    finally:
        cursor.close()
        conn.close()

Note: When working with INSERT, UPDATE and DELETE function we need to perform transaction management. 
      Make sure to commit if successfull or rollback if not.

 ##DELETING RECORD (INSERTING) FROM A DB
    id=int(input("Enter user id:"))
    cusor = conn.cursor()

    try:
        cursor.execute("delete from userinfo where id=%id" %id)
        conn.commit()
    execpt:
        conn.rollback()
    else:
        print("User Information Added Successful")
    finally:
        cursor.close()
        conn.close()

    Note: For production implementation this CRUD functions should be wrapped within a function.
          This provides encapsulation which is a key concept in OOP
"""