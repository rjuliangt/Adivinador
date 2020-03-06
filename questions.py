from gamedb import *

def welcome():
    print('\n\t#######################################\n \
    #################################################\n \
    SOY EL ADIVINADOR DE MEDALLISTAS OLIMPICOS :D \n \
    ###############################################')
    instruction()
    print('\nDeseas jugar?')
    return int(input('1_Si      2_NO'))
    
def instruction():
    print("\n Este juego consiste en darle pistas al ente adividar para que\n \
    logre dar con el medallista en el que estas pensando, puedes salir del juego\n \
    presionando la letra 'O', bueno empecemos :)")    
def frisAsk():
    print('\nacaso el medallista en el que estas pensando es “Erick Barrondo ”?')
    op = int(input('\t1) Si  2)NO :  '))

def askOlympicGame():
    print('\nDe que nacionalidad es el medallista?')
    sql = 'SELECT olympic_games.ID_OLYMPIC_GAME, olympic_games.COUNTRY FROM olympic_games WHERE ID_OLYMPIC_GAME > 0'
    name = selectDB(sql)
    return travelTable(name)
    
def askYearGame():
    sql = 'SELECT olympic_games.ID_OLYMPIC_GAME, olympic_games.YEAR FROM olympic_games WHERE ID_OLYMPIC_GAME > 0'
    print('\nEn que año participo el medallista?')
    year = selectDB(sql)
    return travelTable(year)
    
def askDeport():
    sql = "SELECT deports.ID_DEPORT, deports.NAME_DEPORT FROM deports WHERE deports.ID_DEPORT > 0"
    print('\nEn qué deporte participo el medallista? ')
    name = selectDB(sql)
    return travelTable(name)

def askCategories():
    sql = "SELECT deports.ID_DEPORT, deports.CATEGORIES FROM deports WHERE deports.ID_DEPORT > 0"
    print('\nEn qué Categoria del deporte participo el medallista? ')
    name = selectDB(sql)
    return travelTable(name)

def askNameMedal():
    sql = "SELECT medals.ID_MEDAL, medals.NAME_MEDAL FROM medals WHERE medals.ID_MEDAL > 0"
    print('\nQué tipo de medalla gano? ')
    name = selectDB(sql)
    return travelTable(name)

def askNameCountry():
    sql = "SELECT countries.ID_COUNTRY, countries.NAME_COUNTRY FROM countries WHERE countries.ID_COUNTRY > 0"
    print('\nDe qué país es el medallista? ')
    name = selectDB(sql)
    return travelTable(name)

def askCityCountry():
    sql = "SELECT countries.ID_COUNTRY, countries.CITY FROM countries WHERE countries.ID_COUNTRY > 0"
    print('\nDe que ciudad es el medallista? ')
    name = selectDB(sql)
    return travelTable(name)

def askArea():
    sql = "SELECT countries.ID_COUNTRY, countries.AREA FROM countries WHERE countries.ID_COUNTRY > 0"
    print('\nEn qué area vive el medallista? ')
    name = selectDB(sql)
    return travelTable(name)

def askNamePeople():
    # sql = "SELECT people.ID_PERSON, people.FULL_NAME FROM people WHERE people.ID_PERSON > 0"
    print('\nWOw al parecer no lograre adivinar\n ')
    name = str(input('dime cual es el nombre del medallista? '))
    # name = selectDB(sql)
    return name

def askAgePeople():
    sql = "SELECT people.ID_PERSON, people.AGE FROM people WHERE people.ID_PERSON > 0"
    print('Cuantos años tiene el medallista? ')
    name = selectDB(sql)
    return travelTable(name)

def askGenderPeople():
    sql = "SELECT people.ID_PERSON, people.Gender FROM people WHERE people.ID_PERSON > 0"
    name = selectDB(sql)
    return travelTable(name)

def travelTable(val):
    for nam in val:
        print('\t{}) {}'.format(nam[0],nam[1]))
    return option(val)

def option(table):
    if len(table) == 0:
        print("Sin datos")
    else:
        answer = int(input('\nSelccione su respuesta: '))
        if answer > 0 and answer < len(table)+1:
            print("Respusta: {} {}".format(answer,table[answer-1]))
            return answer,table[answer-1]
        else:
            print("\nNo ingreso un valor correcto")

welcome()
askOlympicGame()
# askCategories()
# askNameMedal()
# askAgePeople()