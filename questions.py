from gamedb import selectDB

import random
def welcome():
    print('\n     #################################################\n \
    #################################################\n \
     SOY EL ADIVINADOR DE MEDALLISTAS OLIMPICOS :D \n \
    #################################################\n     #################################################')
    instruction()
    print('\nDeseas jugar?')
    return int(input('1_Si      2_NO ___'))
    
def instruction():
    print("\n     Este juego consiste en darle pistas al ente adivinador para que\n \
    logre dar con el medallista en el que estas pensando, puedes \n \
    salir del juego presionando la letra 'O', bueno empecemos :)")    

def frisAsk():
    print('\nAcaso el medallista en el que estas pensando es “Erick Barrondo ”?')
    return int(input('\t1) Si  2)NO :  '))
    
def askOlympicGame():
    print('\nEn que Juego Olimpico participo el medallita?')
    sql = 'SELECT olympic_games.ID_OLYMPIC_GAME, olympic_games.COUNTRY FROM olympic_games WHERE ID_OLYMPIC_GAME > 0'
    name = selectDB(sql)
    return travelTable(name)
    
def askYearGame():
    sql = 'SELECT olympic_games.ID_OLYMPIC_GAME, olympic_games.YEAR FROM olympic_games WHERE ID_OLYMPIC_GAME > 0'
    print('\nEn que año participo el medallista?')
    year = selectDB(sql)
    return travelTable(year)
    
def askDeport(id_depo):
    if id_depo == 'null':
        sql = "SELECT deports.ID_DEPORT, deports.NAME_DEPORT FROM deports WHERE deports.ID_DEPORT > 0"
        name = selectDB(sql)
        nu = random.randint(0,len(name)-1)
        return name[nu]
    else:
        sql = "SELECT deports.ID_DEPORT, deports.NAME_DEPORT FROM deports WHERE deports.ID_DEPORT = {}".format(id_depo)
        print('\nEn qué deporte participo el medallista? ')
        name = selectDB(sql)
        return name


def askCategories(id_cat):
    if id_cat == 'null':
        sql = "SELECT categories.ID_CATEGORIES, categories.NAME FROM categories WHERE categories.ID_CATEGORIES > 0"
        name = selectDB(sql)
        nu = random.randint(0,len(name)-1)
        return name[nu]
    else:
        sql = "SELECT categories.ID_CATEGORIES, categories.NAME FROM categories WHERE categories.ID_DEPORT = {}".format(id_cat)
        name = selectDB(sql)
        return name

def askNameMedal(id_med):
    if id_med == 'null':
        sql = "SELECT medals.ID_MEDAL, medals.NAME_MEDAL FROM medals WHERE medals.ID_MEDAL > 0"
        name = selectDB(sql)
        num =random.randint(0, len(name)-1)
        return name[num]
    else:
        sql = "SELECT medals.ID_MEDAL, medals.NAME_MEDAL FROM medals WHERE medals.ID_MEDAL = {}".format(id_med)
        name = selectDB(sql)
        return name

def askNameCountry(id_coun):
    if id_coun == 'null':
        sql = "SELECT countries.ID_COUNTRY, countries.NAME_COUNTRY FROM countries WHERE countries.ID_COUNTRY > 0 "
        name = selectDB(sql)
        num = random.randint(0,len(name)-1)
        return name[num]
    else:
        sql = "SELECT countries.ID_COUNTRY, countries.NAME_COUNTRY, people.ID_COUNTRY, people.GENDER FROM countries,people WHERE countries.ID_COUNTRY = people.ID_COUNTRY AND people.GENDER = '{}'".format(id_coun)
        name = selectDB(sql)
        return name   

def askCity(id_country):
    if id_country == 'null':
        sql = "SELECT people.ID_PERSON, people.CITY FROM people WHERE people.ID_COUNTRY > 0"
        name = selectDB(sql)
        n = random.randint(0,len(name)-1)
        return name[n]
    else:
        sql = "SELECT people.ID_PERSON, people.CITY FROM people WHERE people.ID_COUNTRY = {}".format(id_country)
        name = selectDB(sql)
        return name


def askArea(id_per):
    if id_per == 'null':
        sql = "SELECT people.ID_PERSON, people.AGE FROM people WHERE people.ID_PERSON > 0"
        cons = selectDB(sql)
        ran = random.randint(0,len(cons)-1)
        return cons[ran]    
    else:
        sql = "SELECT people.ID_PERSON, people.AGE FROM people WHERE people.ID_PERSON = {}".format(id_per)
        cons = selectDB(sql)
        return cons

def askNamePeople():
    # sql = "SELECT people.ID_PERSON, people.FULL_NAME FROM people WHERE people.ID_PERSON > 0"
    print('\nWOw al parecer no lograre adivinar\n ')
    name = str(input('dime cual es el nombre del medallista? '))
    # name = selectDB(sql)
    return name

def askAgePeople(id_per):
    if id_per == "null":
        sql = "SELECT people.ID_PERSON, people.AGE FROM people WHERE people.ID_PERSON > 0"
        name = selectDB(sql)
        n = random.randint(0,len(name)-1)
        return name[n]
    else:
        sql = "SELECT people.ID_PERSON, people.AGE FROM people WHERE people.ID_PERSON = {}".format(id_per)
        name = selectDB(sql)
        return name

def askGenderPeople():
    sql = "SELECT people.ID_PERSON, people.Gender FROM people WHERE people.ID_PERSON > 0"
    name = selectDB(sql)
    return travelTable(name)

def travelTable(val):
    for nam in val:
        print('\t{}) {}'.format(nam[0],nam[1]))
        
    

def option2(table):
    if len(table) == 0:
        print("Sin datos")
    else:
        answer = int(input('\nSelccione su respuesta: '))
        if answer > 0 and answer < len(table)+1:
            print("Respusta: {} {}".format(answer,table[answer-1]))
            return answer,table[answer-1]
        else:
            print("\nNo ingreso un valor correcto")

def isGender(gen):
    if gen == 'M':
        ques = '\nEs masculino?'
        print(ques)
        n = option()
        if n == "M":
            return ques, 'M'
        else:
            return ques, "F"
    if gen == "F":
        ques = '\nEs sexo femenino?'
        print(ques)
        n = option()
        if n == 1:
            return ques, "F"
        else:
            return ques, "M"
    if gen == 'null':
        isGender('F')

def isMedals(id_med):
    id_tabl = askNameMedal(id_med)
    ques ="\nEsta pensando en un medallista de {}?".format(id_tabl[0][1])
    print(ques)
    n = option()
    if n == 1:
        return ques, id_tabl[0]
    else:
        return 'null'

def isCountry(id_con):
    id_table = askNameCountry(id_con)
    ques = '\nEsta pensando en un medallista de {} ?'.format(id_table[0][1])
    print(ques)
    n = option()
    if n == 1:
        return ques,id_table[0]
    else:
        return 'null'

def isCity(id_ci):
    id_name= askCity(id_ci)
    ques ="\nEs de la ciudad de {}?".format(id_name[0][1])
    print(ques)
    n = option()
    if n == 1:
        return ques,id_name[0]
    else:
        return 'null'

def isCategories(id_ca):
    id_name = askCategories(id_ca)
    ques ="\nEs de la categoria de {}?".format(id_name[0][1])
    print(ques)
    n = option()
    if n == 1:
        return ques, id_name[0]
    else:
        return 'null'

def isDeport(id_dep):
    id_table = askDeport(id_dep)
    ques ='\nAcaso el medallisata participo en "{}"? '.format(id_table[1]) 
    print(ques)
    n = option()
    if n == 1:
        return ques, id_table[0]
    else:
        return 'null'

def isAge(id_p):
    id_tab = askAgePeople(id_p)
    ques ='\nPiensas en un medallista que nacio en "{}"? '.format(id_tab[1])
    print(ques)
    n = option()
    if n == 1:
        return ques, id_tab[0]
    else:
         return 'null'

def isPeople(id_gen,id_count,id_city):
    sql = "SELECT people.ID_PERSON, people.FULL_NAME, countries.ID_COUNTRY FROM people, countries WHERE people.GENDER = '{0}' AND countries.ID_COUNTRY = {1} AND people.CITY = '{2}'".format(id_gen,id_count,id_city)
    res = selectDB(sql)
    if len(res) == 0:
        print('No hay datos')
        return 'null'
    else:
        # print(f'{res[0][1]}')
        print("\nEs acaso '{}' en quien pensabas?".format(res[0][1]))
        return res

def option():
    n = int(input('1)Si  2)No : '))
    return n



# def isMedals():
#     ques ="\nEsta pensando en un medallista de {}?".format(askNameMedal())
#     print(ques)
#     n = int(input('1)Si  2)No : '))
#     return ques,n

# n = isCountry('null')
# for m in n:
#     print(f'{m}')