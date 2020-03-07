import pymysql

def openConexion():
    try:
        db = pymysql.connect("localhost","root","","gamesdb") # open conexion database
        # cursor = db.cursor() # object for using cursor() method
        # cursor.execute("SELECT VERSION()") # using method execute().
        # value = cursor.fetchone()
        # print("Coneccion establesida base de datos: {}".format(value))
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

def insertDeport(deport,id_game):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO deports(ID_DEPORT,NAME_DEPORT,ID_OLYMPIC_GAME)\
        VALUES(NULL,'{0}',{1})".format(deport,id_game)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertPerson(full_name,age,gender,cit,id_country):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO people(ID_PERSON,FULL_NAME,AGE,GENDER,CITY,ID_COUNTRY)\
        VALUES(NULL,'{0}',{1},'{2}','{3}',{4})".format(full_name,age,gender,cit,id_country)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertWinners(id_person,id_medal,id_deport,id_cat):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO winners(ID_WINNER,ID_PERSON,ID_DEPORT,ID_MEDAL,ID_CATEGORIES)\
        VALUES(NULL,{0},{1},{2},{3})".format(id_person,id_deport,id_medal,id_cat)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')     

def insertCategories(name,id_deport):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor()
        sql = "INSERT INTO categories(ID_CATEGORIES,NAME,ID_DEPORT)\
        VALUES(NULL,'{0}',{1})".format(name,id_deport)
        try:
            cursor.execute(sql)
            db.commit()
            print("\ninsert successful!!!")
        except:
            db.rollback()
            print('insert error')
    else:
        print('error in database')

def insertCountry(name_country,leng,total):
    db =  openConexion()
    if db != 'null':
        cursor = db.cursor() 
        sql = "INSERT INTO countries(ID_COUNTRY,NAME_COUNTRY,LENGUAJE,TOTAL_MEDAL)\
        VALUES(NULL,'{0}','{1}',{2})".format(name_country,leng,total)
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
    db.close()


# insertDeport('Ciclismo',1)
# insertDeport('Badminton',1)
# insertDeport('Gimnasia Artisitica',1)
# insertDeport('Halterofilia',1)
# insertDeport('Judo',1)
# insertDeport('Judo',1)
# insertDeport('Natacion',1)
# insertDeport('Pentatlon Moderno',1)
# insertDeport('Taekwondo',1)
# insertDeport('Tiro',1)
# insertDeport('Vela',1)
# insertDeport('Badminton',1)
# insertDeport('Badminton',1)
# insertDeport('Lucha libre',1)
# insertDeport('Natacion',1)
# insertDeport('Tenis',1)
# insertDeport('Saltos',1)
# insertDeport('Voleibol',1)
# insertDeport('Esgrima',1)
# insertCategories('Espada',20)
# insertCategories('Individual',17)
# insertCategories('100 m vallas F',1)
# insertCategories('400 m vallas F',1)
# insertCategories('75 kg F',7)
# insertCategories('Individual M',2)
# insertCategories('53 kg F',15)
# insertCategories('97 kg M',15)
# insertCategories('100 m libre',8)
# insertCategories('200 m libre',8)
# insertCategories('400 m libre',8)
# insertCategories('800 m libre',8)
# insertCategories('Suelo',4)
# insertCategories('Individual',4)
# insertCategories('Anillo',4)
# insertCategories('80 kg',10)
# insertCategories('Individual',10)
# insertCategories('Individual',11)
# insertCategories('20 km',1)
# insertCategories('50 km',1)
# insertCategories('Singles',3)
# insertCategories('Concurso completo',4)
# insertCategories('Levantamiento de Pesas +75 kg',5)
# insertCategories('Levantamiento de Pesas +105 kg',5)
# insertCategories('Judo 100kg',6)
# insertCategories('Pentatlón',9)
# insertCategories('49 kg',10)
# insertCategories('Foso',11)
# insertCategories('Láser',12)
# insertCategories('Torneo',13)
# insertCategories('86 kg M',15)
# insertCategories('Dobles M',17)
# insertCategories('Plataforma 10 m M',18)
# insertCategories('Sable por eqs. F',20)

# insertMedal('Oro','Amarillo')
# insertMedal('Plata','Gris')
# insertMedal('Bronce','cafe')

# insertPerson('Brianna Rollins',28,'F','Miami',23)
# insertPerson('Erick Barrondo6​',28,'M','',13)
# insertPerson('Mirna Ortiz',33,'F','San Cristobal Verapaz',13)
# insertPerson('Jaime Quiyuch',1988,'M','',13,)
# insertPerson('Mayra Herrrera ',1988,'F','Guatemala',13)
# insertPerson('José Amado García',1977,'M','',13)
# insertPerson('Kevin Cordón',1986,'M','Zacapa',13)
# insertPerson('Manuel Rodas ',1984,'M','Quetzaltenango',13)
# insertPerson('Ana Sofía Gómez',1995,'F','Guatemala',13)
# insertPerson('Kevin Ávila',1992,'M','Zacapa',13)
# insertPerson('Tianna Bartoletta',1985,'F','Ohio',23)
# insertPerson('Claressa Shields',1995,'F','',23)

# insertWinners(1,1,1,36)
# insertWinners(2,2,1,12)
# insertWinners(3,1,1,2)
# insertWinners(4,1,4,28)
# insertWinners(5,1,10,31)
# insertWinners(6,3,17,35)
# insertWinners(7,1,4,30)
# insertWinners(8,2,8,37)
# insertWinners(9,2,11,33)
# insertWinners(10,3,10,32)
# insertWinners(11,1,20,34)
# insertWinners(12,1,4,29)
