import sqlite3 as sl
with sl.connect("space.db") as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE planets""")
    cursor.execute("""DROP TABLE astronauts""")
    cursor.execute("""DROP TABLE space_expedition""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS planets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                number_of_satellites INTEGER NOT NULL
               )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS astronauts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, 
                age INTEGER NOT NULL DEFAULT 21,
                number_of_flights INTEGER NOT NULL
                )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS space_expedition (
               id INTEGER NOT NULL UNIQUE,
               id_planet INTEGER NOT NULL,
               id_astronaut INTEGER NOT NULL,
               report TEXT NOT NULL,
               expedition_time TEXT NOT NULL,
               FOREIGN KEY (id_planet) REFERENCES planets (id),
               FOREIGN KEY (id_astronaut) REFERENCES astronauts (id),
               PRIMARY KEY (id_planet, id_astronaut)
               )""")

    # подготавливаем множественный запрос
    sql1 = 'INSERT INTO planets (name, number_of_satellites) values(?, ?)'
    # указываем данные для запроса
    data1 = [
        ('Меркурий', 0),
        ('Венера', 0),
        ('Земля', 1),
        ('Марс', 2),
        ('Юпитер', 79),
        ('Сатурн', 82),
        ('Уран', 23),
        ('Нептун', 14)
    ]

    sql2 = 'INSERT INTO astronauts (name, age, number_of_flights) values(?, ?, ?)'
    data2 = [
        ('Гагарин Юрий Алексеевич', 34, 1),
        ('Серова Елена Олеговна', 47, 1),
        ('Терешкова Валентина Владимировна', 86, 2),
        ('Титов Владимир Георгиевич', 76, 4),
        ('Маленченко Юрий Иванович', 61, 6),
    ]

    sql3 = 'INSERT INTO space_expedition (id, id_planet, id_astronaut, report, expedition_time) values(?, ?, ?, ?, ?)'
    data3 = [
        (123, 2, 4, 'Высадка на Луну', '17 часов'),
        (674, 4, 2, 'Полёт вокруг Марса', '1 день 10 часов'),
        (901, 5, 3, 'Экспедиция на Юпитер', '10 дней 1 час')
    ]

    # добавляем с помощью множественного запроса все данные сразу
    cursor.executemany(sql1, data1)
    cursor.executemany(sql2, data2)
    cursor.executemany(sql3, data3)

    cursor.execute('SELECT * FROM space_expedition')
    alldata = cursor.fetchall()
    print(alldata)
    cursor.execute("SELECT id, name FROM astronauts WHERE number_of_flights > 4")
    alldata = cursor.fetchall()
    print(alldata)
    cursor.execute("SELECT * FROM planets WHERE name LIKE '%Земля%'")
    alldata = cursor.fetchall()
    print(alldata)
    db.commit()
db.close()

