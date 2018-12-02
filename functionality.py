import pymysql


#### Basic functionality ###
def conn():
    conn = pymysql.connect(host='academic-mysql.cc.gatech.edu',
                           user='cs4400_group17',
                           password='dUdUmYqj',
                           db='cs4400_group17')
    return conn
def login(conn, username, password):
    sql = ("SELECT Username FROM User\
                WHERE Username = '%s'\
                AND Password = '%s'" % (username, password))
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    if result != None:
        return result[0]

def check_regiser(conn, username, email, password1, password2):
    if password1 != password2:
        result = [False, "Password do not match"]
    if len(password1) < 8:
        result = [False, "Password must be 8 characters"]
    try:
        email[email.index("@"):].index(".")
    except:
        result = [False, "Invalid Email"]
    sql = ("SELECT Username FROM User\
                WHERE Username = '%s'" % username)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    if result != None:
        result = [False, "Username already in use!"]
    sql = ("SELECT Username FROM User\
                WHERE Email = '%s'" % email)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    if result != None:
        result = [False, "Email already in use!"]
    else:
        result = [True]
    return result


def register(conn, username, email, password1, password2, userType):
    check = check_regiser(conn, username, email, password1, password2)
    if check[0] == False:
        return check[1]
    password = password1
    sql = ("INSERT INTO User(Email, Username, Password) VALUES ('%s','%s','%s')" % (email, username, password))
    conn.cursor().execute(sql)
    if type == "staff":
        sql = ("INSERT INTO Staff(Username) VALUES ('%s')" % username)
    if type == "visitor":
        sql = ("INSERT INTO Visitor(Username) VALUES ('%s')" % username)
    conn.cursor().execute(sql)
    conn.commit()

#### Visitor Functionality ####
def search_exhibits(conn):
    pass
def log_visit_to_exhibit(conn):
    pass
def see_animal_details(conn):
    pass
def search_for_animals(conn):
    pass
