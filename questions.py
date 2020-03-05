from gamedb import *

def askOlympicGame():
    sql = 'SELECT * FROM olympic_games WHERE ID_OLYMPIC_GAME > 0'
    name = selectDB(sql)
    return travelTable(name)
    
def askYearGame():
    sql = 'SELECT olympic_games.ID_OLYMPIC_GAME, olympic_games.YEAR FROM olympic_games WHERE ID_OLYMPIC_GAME > 0'
    year = selectDB(sql)
    return travelTable(year)
    
def askDeport():
    sql = "SELECT deports.ID_DEPORT, deports.NAME_DEPORT FROM deports WHERE deports.ID_DEPORT > 0"
    name = selectDB(sql)
    return travelTable(name)

def askCategories():
    sql = "SELECT deports.ID_DEPORT, deports.CATEGORIES FROM deports WHERE deports.ID_DEPORT > 0"
    name = selectDB(sql)
    return travelTable(name)

def askNameMedal():
    sql = "SELECT medals.ID_MEDAL, medals.NAME_MEDAL FROM medals WHERE medals.ID_MEDAL > 0"
    name = selectDB(sql)
    return travelTable(name)

def askName():
    sql = "SELECT countries.ID_COUNTRY, countries.NAME_COUNTRY FROM countries WHERE countries.ID_COUNTRY > 0"
    name = selectDB(sql)
    return travelTable(name)

def askCity():
    sql = "SELECT countries.ID_COUNTRY, countries.CITY FROM countries WHERE countries.ID_COUNTRY > 0"
    name = selectDB(sql)
    return travelTable(name)

def travelTable(val):
    for nam in val:
        print('\t{}) {}'.format(nam[0],nam[1]))
    return option(val)

def option(table):
    answer = int(input('\nSelccione su respuesta: '))
    if answer > 0 and answer < len(table)+1:
        print("Respusta: {}".format(answer))
        return answer
    else:
        print("No ingreso un valor correcto")

# askOlympicGame()
# askCategories()
# askNameMedal()
# askNameMedal()
askCity()