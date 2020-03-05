import pymysql

def openConexion():
    try:
        db = pymysql.connect("localhost","root","","gamesdb") # open conexion database
        cursor = db.cursor() # object for using cursor() method
        cursor.execute("SELECT VERSION()") # using method execute().
        value = cursor.fetchone()
        print("Coneccion establesida base de datos: {}".format(value))
        return db
        # db.close() #disconect to database
    except:
        print("Conexion error")
        return 'null'

def closeConexion(db):
    db.close
    print("Conecction terminated")

def insertOlympicGame(country,name,year):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO olympic_games(ID_OLYMPIC_GAME,COUNTRY,NAME,YEAR)\
        VALUES(NULL,'{0}','{1}','{2}')".format(country,name,year)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertMedal(medals,color):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO medals(ID_MEDAL,NAME_MEDAL,COLOR)\
        VALUES(NULL,'{0}','{1}')".format(medals,color)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertDeport(deport,cate,id_game):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO deports(ID_DEPORT,NAME_MEDAL,CATEGORIES,ID_OLYMPIC_GAME)\
        VALUES(NULL,'{0}','{1}',{2})".format(deport,cate,id_game)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertPerson(full_name,age,gender,id_country):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO people(ID_PERSON,FULL_NAME,AGE,GENDER,ID_COUNTRY)\
        VALUES(NULL,'{0}','{1}','{2}',{3})".format(full_name,age,gender,id_country)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertWinners(id_person,id_medal,id_deport):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO winners(ID_WINNER,ID_PERSON,ID_DEPORT,ID_MEDAL)\
        VALUES(NULL,{0},{1},{2})".format(id_person,id_deport,id_medal)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')     
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO people(ID_PERSON,NAME,AGE,GENDER,ID_COUNTRY)\
        VALUES(NULL,'{0}','{1}',{2})".format(full_name,age,gender,id_country)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertCountry(name_country,city,leng,area):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor() 
        sql = "INSERT INTO countries(ID_COUNTRY,NAME_COUNTRY,CITY,LENGUAJE,AREA)\
        VALUES(NULL,'{0}','{1}','{2}','{3}')".format(name_country,city,leng,area)
        try:
            cursor.execute(sql) #Execute sql insert
            db.commit()         # Commit in the database
            print("\ninsert successful!!!")
        except:
            db.rollback()       # Rollback if there is error
            print('insert error')
    else:
        print('error in database')       

def selectDB(sql_select):
    db = openConexion()
    cursor = db.cursor()
    try:
        cursor.execute(sql_select) #Execute sql select
        result = cursor.fetchall()
        return result
        # print("\nid:    name:         country:          year:")
        # for val in result:
        #     ide = val[0]
        #     country =val[1]
        #     name = val[2]
        #     year = val[3]
        #     print("{}   | {}        | {}         | {}".format(ide,country,name,year))

    except:
        print('Error in select')



