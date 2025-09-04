import mysql.connector
from Config import *

def insert_CUSTOMER_data(custid, phone, email, orderscount = None):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    if orderscount is None:
        orderscount = 0
    SQL_Query = "INSERT INTO CUSTOMER (ID ,PHONE,EMAIL, ORDERSCOUNT) VALUES (%s, %s, %s, %s);"
    cur.execute(SQL_Query, (custid, phone, email, orderscount))
    connection.commit()
    cur.close()
    connection.close()
    print(f'Customer data id: {custid} inserted successfully')


def insert_ADMIN_data(adminid, phone, acceptedorders= None):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    if acceptedorders is None:
        acceptedorders = 0
    SQL_Query = "INSERT INTO ADMIN (ID, PHONE, ACCEPTEDORDERS) VALUES (%s, %s, %s);"
    cur.execute(SQL_Query, (adminid, phone,acceptedorders))
    connection.commit()
    cur.close()
    connection.close()
    print(f"Admin data id: {adminid} successfully inserted")





def insert_GAMESECTION_data(id, gamename, company):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    SQL_Query = "INSERT INTO GAMESECTION (ID, GAMENAME, COMPANY) VALUES (%s, %s, %s);"
    cur.execute(SQL_Query, (id, gamename, company))   
    connection.commit()
    cur.close()
    connection.close()
    print(f"Gamesection data id: {id} successfully inserted")



def insert_PRODUCT_data(Gasec_ID ,Prod_name, Prod_price):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    SQL_Query = "INSERT INTO PRODUCT (GASEC_ID,PROD_NAME,PROD_PRICE) VALUES (%s, %s, %s);"
    cur.execute(SQL_Query, (Gasec_ID ,Prod_name, Prod_price))
    product_id = cur.lastrowid   
    connection.commit()
    cur.close()
    connection.close()
    print(f"Product data id:{product_id} successfully inserted")
    return product_id



def insert_ORDERS_data(id, transactionphoto,cust_id, admin_id, prod_id, date= None):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    if date is None:
        SQL_Query = "INSERT INTO ORDERS (ID, TRNSACTIONPHOTO, CUST_ID, ADMIN_ID, PROD_ID) VALUES (%s, %s, %s, %s, %s);"
        values = (id, transactionphoto, cust_id, admin_id, prod_id)
    else:
        SQL_Query = "INSERT INTO ORDERS (ID, TRNSACTIONPHOTO, CUST_ID, ADMIN_ID, PROD_ID, DATE) VALUES (%s, %s, %s, %s, %s, %s);"
        values = (id, transactionphoto, cust_id, admin_id, prod_id, date)
    cur.execute(SQL_Query, values)
    connection.commit()
    cur.close()
    connection.close()
    print(f"ORDERS data id {id} successfully inserted")





#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#UPDATE DATA!





def update_CUSTOMER_phonenumber(customerid, new_phonenumber):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()

    SQL_Query = 'UPDATE CUSTOMER SET PHONE = %s WHERE ID = %s;'
    values = (new_phonenumber, customerid)
    cur.execute(SQL_Query, values)
    connection.commit()
    cur.close()
    connection.close()
    print(f"Phonenumber user id {customerid} successfully updated, new phone number: {new_phonenumber}")



def update_CUSTOMER_email(customerid, new_email):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()

    SQL_Query = 'UPDATE CUSTOMER SET EMAIL = %s WHERE ID = %s;'
    values = (new_email, customerid)
    cur.execute(SQL_Query, values)
    connection.commit()
    cur.close()
    connection.close()
    print(f"Email user id {customerid} successfully updated, new email: {new_email}")
    


def update_ADMIN_phonenumber(adminid, new_phonenumber):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()

    SQL_Query = 'UPDATE ADMIN SET PHONE = %s WHERE ID = %s;'
    values = (new_phonenumber, adminid)
    cur.execute(SQL_Query, values)
    connection.commit()
    cur.close()
    connection.close()
    print(f"Phonenumber admin id {adminid} successfully updated, new phone number: {new_phonenumber}")
    



def update_CUSTOMER_orderscount(customerid, new_orderscount):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    SQL_Query = 'UPDATE CUSTOMER SET ORDERSCOUNT = %s WHERE ID = %s;'
    values = (new_orderscount, customerid)
    cur.execute(SQL_Query, values)
    connection.commit()
    cur.close()
    connection.close()
    print(f"Orderscount user id {customerid} successfully updated, new orderscount: {new_orderscount}")
    



def update_ADMIN_orderscount(adminid, new_acceptedorders):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()

    SQL_Query = 'UPDATE ADMIN SET ACCEPTEDORDERS = %s WHERE ID = %s;'
    values = (new_acceptedorders, adminid)
    cur.execute(SQL_Query, values)
    connection.commit()
    cur.close()
    connection.close()
    print(f"Accepted orders count admin id {adminid} successfully updated, new orderscount: {new_acceptedorders}")



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



#DELETE DATA!




def delete_PRODUCT_data(productid):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    query = "DELETE FROM PRODUCT WHERE ID = %s"
    cur.execute(query, (productid,))
    connection.commit()
    cur.close()
    connection.close()
    print(f"Deleted product ID {productid} from database successfully")




def delete_ADMIN_data(adminid):
    connection = mysql.connector.connection.MySQLConnection(**config)
    cur = connection.cursor()
    query = "DELETE FROM ADMIN WHERE ID = %s"
    cur.execute(query, (adminid,))
    connection.commit()
    cur.close()
    connection.close()
    print(f"Deleted admin ID {adminid} from database successfully")


