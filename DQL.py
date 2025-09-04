import mysql.connector
from Config import *

def get_CUSTOMER_data(id):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM CUSTOMER WHERE ID=%s"
    cur.execute(SQL_Query, (id,))
    cu_result = cur.fetchone()
    cur.close()
    conn.close()
    return cu_result


def get_ADMIN_data(id):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM ADMIN WHERE ID=%s"
    cur.execute(SQL_Query, (id,))
    ad_result = cur.fetchone()
    cur.close()
    conn.close()
    return ad_result


def get_ORDERS_data(orderid):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM ORDERS WHERE ID=%s"
    cur.execute(SQL_Query, (orderid,))
    sa_result = cur.fetchone()
    cur.close()
    conn.close()
    return sa_result


def get_GAMESECTION_data(gamename):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM GAMESECTION WHERE GAMENAME=%s"
    cur.execute(SQL_Query, (gamename,))
    ga_result = cur.fetchone()
    cur.close()
    conn.close()
    return ga_result


def get_PRODUCT_data_by_name(prodname):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM PRODUCT WHERE PROD_NAME=%s"
    cur.execute(SQL_Query, (prodname,))
    pr_result = cur.fetchone()
    cur.close()
    conn.close()
    return pr_result

def get_PRODUCT_data_by_id(prodid):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM PRODUCT WHERE ID=%s"
    cur.execute(SQL_Query, (prodid,))
    pr_result = cur.fetchone()
    cur.close()
    conn.close()
    return pr_result




def get_ALLPRODUCT_data_in_GAMESECTION(GamesectionID):
    conn = mysql.connector.connection.MySQLConnection(**config)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM PRODUCT WHERE GASEC_ID = %s"
    cur.execute(SQL_Query, (GamesectionID,))
    apr_result = cur.fetchall()
    cur.close()
    conn.close()
    return apr_result
