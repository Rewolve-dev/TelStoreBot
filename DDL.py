import mysql.connector
from Config import *

def create_n_drop():
    connection = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'])
    cur = connection.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {DATABASE};")
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE};")
    connection.commit()
    cur.close()
    connection.close()
    print(f'database {DATABASE} created successfully')



def createtableUSERS():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("""
    CREATE TABLE USERS (
    ID              BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    REGISTER_DATE   DATETIME DEFAULT CURRENT_TIMESTAMP,
    LAST_UPDATE     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

""")    
    print("table USERS created")


def createtableCUSTOMER():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("""
    CREATE TABLE CUSTOMER (
    ID              BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    EMAIL           VARCHAR(200) NOT NULL,
    PHONE           VARCHAR(20) NOT NULL UNIQUE,
    ORDERSCOUNT     INT NOT NULL DEFAULT 0,
    REGISTER_DATE   DATETIME DEFAULT CURRENT_TIMESTAMP,
    LAST_UPDATE     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

""")    
    print("table customer created")


def createtableADMIN():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("""
CREATE TABLE ADMIN (
ID                  BIGINT UNSIGNED NOT NULL PRIMARY KEY,
PHONE               VARCHAR(15) NOT NULL UNIQUE,
ACCEPTEDORDERS      INT NOT NULL DEFAULT 0,
REGISTER_DATE       DATETIME DEFAULT CURRENT_TIMESTAMP,
LAST_UPDATE         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

""")
    
    print("table admin created")





def createtableGAMESECTION():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("""
CREATE TABLE GAMESECTION(
ID                  MEDIUMINT UNSIGNED NOT NULL PRIMARY KEY,
GAMENAME            VARCHAR(100) NOT NULL UNIQUE,
COMPANY             VARCHAR(50),
REGISTER_DATE       DATETIME DEFAULT CURRENT_TIMESTAMP,
LAST_UPDATE         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

                );
""")
    print("table gamesection created")



def createtablePRODUCT():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("""
CREATE TABLE PRODUCT (
ID                  MEDIUMINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
GASEC_ID            MEDIUMINT UNSIGNED,
PROD_NAME           VARCHAR(200) NOT NULL UNIQUE,
PROD_PRICE          VARCHAR(50) NOT NULL,
FOREIGN KEY         (GASEC_ID) REFERENCES GAMESECTION(ID),
REGISTER_DATE       DATETIME DEFAULT CURRENT_TIMESTAMP,
LAST_UPDATE         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

                );
""")
    print("table product created")



def createtableORDERS():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("""
CREATE TABLE ORDERS (
ID                  BIGINT UNSIGNED NOT NULL PRIMARY KEY,
TRNSACTIONPHOTO     BIGINT UNSIGNED NOT NULL,
DATE                DATETIME NOT NULL,
CUST_ID             BIGINT UNSIGNED,
ADMIN_ID            BIGINT UNSIGNED,
PROD_ID             MEDIUMINT UNSIGNED,
FOREIGN KEY         (CUST_ID) REFERENCES CUSTOMER(ID),
FOREIGN KEY         (ADMIN_ID) REFERENCES ADMIN(ID),
FOREIGN KEY         (PROD_ID) REFERENCES PRODUCT(ID),
REGISTER_DATE       DATETIME DEFAULT CURRENT_TIMESTAMP,
LAST_UPDATE         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
""")
    print("table ORDERS created")


if __name__ == "__main__":
    create_n_drop()
    createtableCUSTOMER()
    createtableADMIN()
    createtableGAMESECTION()
    createtablePRODUCT()
    createtableORDERS()
    createtableUSERS()