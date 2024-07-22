"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """

    count = 0
    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            count += int(i[1])

    return count

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    
    letters = []
    count = []

    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            letters.append(i[0])
    for j in set(letters):
        count.append((j, letters.count(j)))
    count.sort()

    return count


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    
    """
    answer = []
    count = []
    letters = []

    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            if(not i[0] in letters):
                letters.append(i[0])
                count.append(int(i[1]))
            else:
                count[letters.index(i[0])]+=int(i[1])
    for j in letters:
        answer.append((j,count[letters.index(j)]))
    answer.sort(reverse=False)

    return answer


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    months = []
    answer = []

    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            month = i[2].split("-")[1]
            months.append(month)
    for month in sorted(set(months)):
        answer.append((month, months.count(month)))

    return answer


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    letters = []
    count = []
    answer = []

    with open('data.csv') as csv_file:
        data = csv.reader(csv_file, delimiter='	')
        for i in data:
            if not i[0] in letters:
                letters.append(i[0])
                count.append([int(i[1])])
            else:
                count[letters.index(i[0])].append(int(i[1]))
    
    for j in sorted(set(letters)):
        answer.append((j, max(count[letters.index(j)]), min(count[letters.index(j)])))  
    return answer


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """

    stringls = []
    values = []
    answer = []
    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            dic = i[4].split(',')
            for j in dic: 
                cadena = j.split(':')[0]
                valor = j.split(':')[1]
                if cadena not in stringls:
                    stringls.append(cadena)
                    values.append([int(valor)])
                else:
                    values[stringls.index(cadena)].append(int(valor))
    for cadena in sorted(stringls):
        answer.append((cadena, min(values[stringls.index(cadena)]), max(values[stringls.index(cadena)])))

    return answer

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """

    numbers = []
    letters = []
    answer = []

    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            if int(i[1]) not in numbers:
                numbers.append(int(i[1]))
                letters.append([i[0]])
            else:
                letters[numbers.index(int(i[1]))].append(i[0])
    for j in sorted(numbers):
        answer.append((j, letters[numbers.index(j)]))
    return answer


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """

    numbers = []
    answer = []
    letters = []

    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            if int(i[1]) not in numbers:
                numbers.append(int(i[1]))
                letters.append({i[0]})
            else:
                letters[numbers.index(int(i[1]))].add(i[0])
    for j in sorted(numbers):
        answer.append((j, list(sorted(letters[numbers.index(j)]))))
    answer.sort()
    
    return answer

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """

    dicc = {}
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for i in datos:
            dictionary = i[4].split(',')
            for j in dictionary: 
                cadena = j.split(':')[0]

                if cadena not in dicc.keys():
                    dicc[cadena] = 1
                else:
                    dicc[cadena] += 1
    answer = dict(sorted(dicc.items()))
    
    return answer


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """

    answer = []
    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            var1 = len(i[3].split(','))
            var2 = len(i[4].split(','))
            answer.append((i[0], var1, var2))
        
    return answer


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """

    letters = {}
    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            for j in i[3].split(','):
                if not j in letters.keys():
                    letters[j] = int(i[1])
                else:
                    letters[j] += int(i[1])
    answer = dict(sorted(letters.items()))

    return answer


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """

    letters = {}
    with open('data.csv') as data:
        data = csv.reader(data, delimiter='	')
        for i in data:
            letter = i[0]
                
            for j in i[4].split(','):
                var1 = int(j.split(':')[1])

                if not letter in letters.keys():
                    letters[letter] = var1
                else:
                    letters[letter] += var1
    answer = dict(sorted(letters.items()))

    return answer
