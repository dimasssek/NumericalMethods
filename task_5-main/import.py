import xml.dom.minidom as minidom
import sqlite3 as sq

file = open('import_data.xml', encoding='UTF-8')
dom = minidom.parse(file)
dom.normalize()
elements = dom.getElementsByTagName('planet')
name = []
id_p = []
number_of_satellites = []
for node in elements:
    name_planet = node.getAttribute("name")
    name.append(name_planet)
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'id':
                id_p.append(child.firstChild.data)
            if child.tagName == 'number_of_satellites':
                number_of_satellites.append(child.firstChild.data)

with sq.connect("space.db") as db:
    cursor = db.cursor()
    for i in range(len(name)):
        cursor.execute('INSERT INTO planets VALUES(?,?,?)', (id_p[i], name[i], number_of_satellites[i]))
        db.commit()
file.close()