
import mysql.connector
from mysql.connector import pooling
from mysql.connector.pooling import MySQLConnectionPool



dbconfig={
'host':'localhost',
'user':'root',
'password':'',
'database':'one_day_trip'
}


pool=mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=32,
    **dbconfig
)
