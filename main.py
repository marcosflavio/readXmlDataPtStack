import xml.etree.ElementTree as ET
import MySQLdb
tree = ET.parse('/home/marcos/pt stack/Badges.xml')
root = tree.getroot()
print(root.tag)
count = 0
for row in root.findall('row'):
    count = count + 1
    name = row.get('Name')
    id = row.get('Id')
    userId = row.get('UserId')
    date = row.get('Date')
    clas = row.get('Class')
    tagBased = row.get('TagBased')

    print name, id, userId, date, clas, tagBased
print count

# db = MySQLdb.connect(host="localhost", user="root", passwd="root",
# db="")