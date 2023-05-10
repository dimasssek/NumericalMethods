#!/usr/bin/env python3
import cgi
import sqlite3 as sq

form = cgi.FieldStorage()
n_p = form.getfirst("name_p")
n_s = form.getfirst("num_s")
n_a = form.getfirst("name_a")
age = form.getfirst("age")
n_f = form.getfirst("num_f")
print("Content-type: text/html; charset=utf-8\n")
if (n_p and n_s):
    print(f"{n_p} -> {n_s}")
    with sq.connect("space.db") as db:
        cursor = db.cursor()
        cursor.execute('INSERT INTO planets VALUES(NULL,?,?)', (n_p, n_s))
        db.commit()
        print("""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Успех</title>
                        </head>
                        <body>
                            <a href="../../index.html"><p>Назад</p></a>


                        </body>
                        </html>
                """)
        cursor.execute('SELECT * FROM planets')
        alldata = cursor.fetchall()
        print(f"""<table>
                   <tr>
                   <td>id</td>
                   <td>Название</td>
                   <td>Количество спутников</td>
                   </tr>""")
        for cur in alldata:
            print(f"""
                     <tr>
                       <td>{cur[0]}</td>
                       <td>{cur[1]}</td>
                       <td>{cur[2]}</td>
                     </tr>""")
        print("""</table>""")

else:
    if (n_a and age and n_f):
        print(f"{n_a} -> {age} -> {n_f}")
        with sq.connect("space.db") as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO astronauts VALUES(NULL,?,?)', (n_a, age, n_f))
            db.commit()
            print("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>Успех</title>
                            </head>
                            <body>
                                <a href="../../index.html"><p>Назад</p></a>
                                <p></p>
                            </body>
                            </html>
            """)
            cursor.execute('SELECT * FROM astronauts')
            alldata = cursor.fetchall()
            print(f"""<table>
            <tr>
            <td>id</td>
            <td>ФИО</td>
            <td>Возраст</td>
            <td>Количество полётов</td>
            </tr>""")
            for cur in alldata:
                print(f"""
              <tr>
                <td>{cur[0]}</td>
                <td>{cur[1]}</td>
                <td>{cur[2]}</td>
              </tr>""")
            print("""</table>""")


    else:
        print("Форма была не полностью заполнена, попробуйте еще раз")
        print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>Не получилось</title>
                </head>
                <body>
                    <a href="../../index.html"><p>Назад</p></a>
                </body>
                </html>
        """)
