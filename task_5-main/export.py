import xml.dom.minidom as minidom
import sqlite3 as sq

root = minidom.Document()
xml = root.createElement('planets')
root.appendChild(xml)
with sq.connect("space.db") as db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM planets')
    for cur in cursor:
        new_planet = root.createElement('planet')
        new_planet.setAttribute("name", cur[1])
        new_id = root.createElement("id")
        new_id_data = root.createTextNode(str(cur[0]))
        new_id.appendChild(new_id_data)
        new_number_of_satellites = root.createElement("number_of_satellites")
        new_number_of_satellites_data = root.createTextNode(str(cur[2]))
        new_number_of_satellites.appendChild(new_number_of_satellites_data)
        new_planet.appendChild(new_id)
        new_planet.appendChild(new_number_of_satellites)
        xml.appendChild(new_planet)
out_byte = root.toprettyxml(encoding='UTF-8')
out_text = out_byte.decode("UTF-8")
save_path_file = "export_data.xml"
with open(save_path_file, "w", encoding="UTF-8") as f:
    f.write(out_text)
f.close()