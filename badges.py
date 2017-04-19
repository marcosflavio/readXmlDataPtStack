import xml.etree.ElementTree as ET
import csv
tree = ET.parse('/home/marcos/pt stack/Badges.xml')
root = tree.getroot()
count = 0
header = ('Id', 'UserId', 'Name', 'Date', 'Class', 'TagBased')
with open('/home/marcos/pt stack/badgesOutput.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    id = ''
    userId = ''
    name = ''
    date = ''
    clas = ''
    tagBased = ''
    for row in root.findall('row'):
        if(row.get('Id') != None):
            id = row.get('Id')
        if(row.get('UserId') != None):
            userId = row.get('UserId')
        if(row.get('Name') != None):
            name = row.get('Name')
        if(row.get('Date')!= None):
            date = row.get('Date')
        if(row.get('Class') != None):
            clas = row.get('Class')
        if(row.get('TagBased') != None):
            tagBased = row.get('TagBased')
        id = id.encode('ascii', 'ignore').decode('ascii')
        userId = userId.encode('ascii', 'ignore').decode('ascii')
        name = name.encode('ascii', 'ignore').decode('ascii')
        date = date.encode('ascii', 'ignore').decode('ascii')
        clas = clas.encode('ascii', 'ignore').decode('ascii')
        tagBased = tagBased.encode('ascii', 'ignore').decode('ascii')
        line = id, userId, name, date, clas, tagBased
        writer.writerow(line)
