import pymysql
import functionality as c

conn = pymysql.connect(host='academic-mysql.cc.gatech.edu',
                       user='cs4400_group17',
                       password='dUdUmYqj',
                       db='cs4400_group17')
if conn.open:
    print("Good conn")

print(c.login(conn, "benjamin_rao","password2"))
print(c.check_regiser(conn, "ben", "marthajohnson@hotmail.com","aaaaaaaa","aaaaaaaa"))

try:
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `User`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()
