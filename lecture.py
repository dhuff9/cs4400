import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='acacademic-mysql.cc.gatech.edu',
                             user='dhuff9',
                             port=3306,
                             password='35499F22a05',
                             db='testdb1')

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql =  "CREATE TABLE IF NOT EXISTS sdata(Date INT, Open DECIMAL(18, 4), High DECIMAL(18, 4), Low DECIMAL(18, 4), Close DECIMAL(18, 4), Volume INT)"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT Date High FROM sdata"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    with connection.cursor() as cursor:
        sql = "DROP TABLE IF EXSITS sdata"
        cursor.execute(sql)
        connection.commit()

finally:
    connection.close()
