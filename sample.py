import threading
import pandas as pd
import time
import mysql.connector
cnx = mysql.connector.connect(
    host="mysql.selfmade.ninja",
    user="iorProject",
    password="iorProject",
    database="iorProject_1"     
)
cursor = cnx.cursor()
def toMySql(dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10):
    query = "INSERT INTO iot (dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10) VALUES (%s, %s, %s, %s, %s)"
    values = (dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()

def save_log():
    with open('Air_pon.csv', 'a') as log:
        pmt_2_5, pmt_10 = get_data()
        aqi_2_5, aqi_10 = conv_aqi(pmt_2_5, pmt_10)
        dt = datetime.now()
        log.write("{}, {}, {}, {}, {}\n".format(dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10))
        sensor_data = (dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10)
        log.close()

def threadFunc():
    t1 = threading.Thread(target=save_log)
    t1.start()
    sensor_data1 = "dt"
    sensor_data2 = "pmt_2_5"
    sensor_data3 = "pmt_10"
    sensor_data4 = "aqi_2_5"
    sensor_data5 = "aqi_10"
    t2 = threading.Thread(target=toMySql, args=(sensor_data1, sensor_data2, sensor_data3, sensor_data4, sensor_data5))
    t2.start()


