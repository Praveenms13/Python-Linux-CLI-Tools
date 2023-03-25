import threading
import mysql.connector
# pip install mysql-connector-python
cnx = mysql.connector.connect(
    host="mysql.selfmade.ninja",
    user="",
    password="",
    database=""     
)
cursor = cnx.cursor()
def toMySql(dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10):
    query = "INSERT INTO iot (dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10) VALUES (%s, %s, %s, %s, %s)"
    values = (dt, pmt_2_5, pmt_10, aqi_2_5, aqi_10)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()

def read_sensor_data():
    sensor_data1 = "data1"
    sensor_data2 = "data2"
    sensor_data3 = "data3"
    sensor_data4 = "data4"
    sensor_data5 = "data5"

    t2 = threading.Thread(target=toMySql, args=(sensor_data1, sensor_data2, sensor_data3, sensor_data4, sensor_data5))
    t2.start()

if __name__ == '__main__':
    read_sensor_data()