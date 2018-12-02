import pymysql
import csv
import datetime


with open("user.csv", "r") as fin:
        csvin = csv.reader(fin)
        keys = ["username","password","email","type"]
        user = [{keys[j]:i[j] for j in range(len(i))} for i in csvin]
with open("animal.csv", "r") as fin:
        csvin = csv.reader(fin)
        keys = ["name","type","species","age","housed"]
        animal = [{keys[j]:i[j] for j in range(len(i))} for i in csvin]
        for i in animal:
            i["age"] = int(i['age'][0:1])
with open("exhibit.csv", "r") as fin:
        csvin = csv.reader(fin)
        keys = ["name","water_feature","size"]
        exhibit = [{keys[j]:i[j] for j in range(len(i))} for i in csvin]
        for i in exhibit:
            i["size"] = int(i["size"])
            if i["water_feature"] == "Yes":
                i["water_feature"] = True
            else:
                i["water_feature"] = False
with open("show.csv", "r") as fin:
        csvin = csv.reader(fin)
        keys = ["name","date_time","host","located"]
        shows = [{keys[j]:i[j] for j in range(len(i))} for i in csvin]
        for i in shows:
            i["date_time"] = datetime.datetime.strptime(i["date_time"],"%m/%d/%y %I:%M%p")

def user_init(conn, username, password, email, type):
    sql = ("INSERT INTO User(Email, Username, Password) VALUES ('%s','%s','%s')" % (email, username, password))
    conn.cursor().execute(sql)
    if type == "admin":
        sql = ("INSERT INTO Admin(Username) VALUES ('%s')" % username)
    if type == "staff":
        sql = ("INSERT INTO Staff(Username) VALUES ('%s')" % username)
    if type == "visitor":
        sql = ("INSERT INTO Visitor(Username) VALUES ('%s')" % username)
    conn.cursor().execute(sql)
def animal_init(conn, name, type, species, age, housed):
    sql = ("INSERT INTO Animal(Name, Type, Species, Age, Housed) VALUES ('%s','%s','%s','%d','%s')" % (name, type, species, age, housed))
    conn.cursor().execute(sql)
    #print(sql)
def exhibit_init(conn, name, water_feature, size):
    sql = ("INSERT INTO Exhibit(Name, Water_Feature, Size) VALUES ('%s',%s,'%d')" % (name, water_feature, size))
    conn.cursor().execute(sql)
    #print(sql)
def shows_init(conn, name, date_time, host, located):
    sql = ("INSERT INTO Shows(Name, Date_Time, Host, Located) VALUES ('%s','%s','%s','%s')" % (name, date_time, host, located))
    conn.cursor().execute(sql)
    #print(sql)



# print(user)
# print(animal)
# print(exhibit)
# print(shows)

conn = pymysql.connect(host='academic-mysql.cc.gatech.edu',
                       user='cs4400_group17',
                       password='dUdUmYqj',
                       db='cs4400_group17')
if conn.open:
    print("Good conn")

conn.cursor().execute("DROP TABLE IF EXISTS User")
conn.cursor().execute("DROP TABLE IF EXISTS Staff")
conn.cursor().execute("DROP TABLE IF EXISTS Visitor")
conn.cursor().execute("DROP TABLE IF EXISTS Admin")
conn.cursor().execute("DROP TABLE IF EXISTS Exhibit")
conn.cursor().execute("DROP TABLE IF EXISTS Shows")
conn.cursor().execute("DROP TABLE IF EXISTS Animal")
conn.cursor().execute("DROP TABLE IF EXISTS EVisits")
conn.cursor().execute("DROP TABLE IF EXISTS SVisits")
conn.cursor().execute("DROP TABLE IF EXISTS Note")



conn.cursor().execute("CREATE TABLE IF NOT EXISTS User(Email varchar(50) NOT NULL, \
                        Username varchar(50) NOT NULL, \
                        Password varchar(50) NOT NULL,\
                        PRIMARY KEY (Username),\
                        UNIQUE (Email))")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Staff(Username varchar(50) NOT NULL,\
                            PRIMARY KEY (Username),\
                            FOREIGN KEY (Username)\
                            REFERENCES User (Username)\
                            ON DELETE CASCADE\
                            ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Visitor(Username varchar(50) NOT NULL,\
                        PRIMARY KEY (Username),\
                        FOREIGN KEY (Username)\
                        REFERENCES User (Username)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Admin(Username varchar(50) NOT NULL,\
                        PRIMARY KEY (Username),\
                        FOREIGN KEY (Username)\
                        REFERENCES User (Username)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Exhibit(Name varchar(50) NOT NULL, \
                        Size int NOT NULL,\
                        Water_Feature boolean NOT NULL,\
                        PRIMARY KEY (Name))")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Shows(Name varchar(50) NOT NULL,\
                        Date_Time datetime NOT NULL,\
                        Host varchar(50) NOT NULL,\
                        Located varchar(50) NOT NULL,\
                        PRIMARY KEY (Name, Date_Time),\
                        FOREIGN KEY (Host)\
                        REFERENCES Staff (Username)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Located)\
                        REFERENCES Exhibit (Name)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Animal(Name varchar(50) NOT NULL,\
                        Species varchar(50) NOT NULL,\
                        Type varchar(50) NOT NULL,\
                        Age int NOT NULL,\
                        Housed varchar(50) NOT NULL,\
                        PRIMARY KEY (Name, Species),\
                        FOREIGN KEY (Housed)\
                        REFERENCES Exhibit (Name)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS EVisits(Date_Time datetime NOT NULL,\
                        Visitor varchar(50) NOT NULL,\
                        Exhibit_Name varchar(50) NOT NULL,\
                        PRIMARY KEY (Date_Time, Visitor, Exhibit_Name),\
                        FOREIGN KEY (Visitor)\
                        REFERENCES Visitor (Username)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Exhibit_Name)\
                        REFERENCES Exhibit (Name)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS SVisits(Visitor varchar(50) NOT NULL,\
                        Exhibit_Name varchar(50) NOT NULL,\
                        Show_Name varchar(50) NOT NULL,\
                        Show_Date_Time datetime NOT NULL,\
                        PRIMARY KEY (Visitor, Exhibit_Name, Show_Name, Show_Date_Time),\
                        FOREIGN KEY (Visitor)\
                        REFERENCES Visitor (Username)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Exhibit_Name)\
                        REFERENCES Exhibit (Name)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Show_Name)\
                        REFERENCES Shows (Name)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Show_Date_Time)\
                        REFERENCES Shows (Date_Time)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

conn.cursor().execute("CREATE TABLE IF NOT EXISTS Note(Text varchar(200) NOT NULL,\
                        Date_Time datetime NOT NULL,\
                        Staff_Username varchar(50) NOT NULL,\
                        Animal_Name varchar(50) NOT NULL,\
                        Animal_Species varchar(50) NOT NULL,\
                        PRIMARY KEY (Staff_Username, \
                        Animal_Name, Animal_Species, Date_Time),\
                        FOREIGN KEY (Staff_Username)\
                        REFERENCES Staff (Username)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Animal_Name)\
                        REFERENCES Animal (Name)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE,\
                        FOREIGN KEY (Animal_Species)\
                        REFERENCES Animal (Species)\
                        ON DELETE CASCADE\
                        ON UPDATE CASCADE)")

for i in user:
    user_init(conn, i["username"], i["password"], i["email"], i["type"])
for i in animal:
    animal_init(conn, i["name"], i["type"], i["species"], i["age"], i["housed"])
for i in exhibit:
    exhibit_init(conn, i["name"], i["water_feature"], i["size"])
for i in shows:
    shows_init(conn, i["name"], i["date_time"], i["host"], i["located"])
conn.commit()
conn.close()
