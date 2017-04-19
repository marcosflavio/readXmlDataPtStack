import xml.etree.ElementTree as ET
import csv
tree = ET.parse('/home/marcos/pt stack/Tags.xml')
root = tree.getroot()
header = ('Id', 'TagName', 'Count')
with open('/home/marcos/pt stack/tagsOutput.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    id = ''
    tagName = ''
    count = ''
    for row in root.findall('row'):
        if(row.get('Id') != None):
            id = row.get('Id')
        if(row.get('TagName') != None):
            tagName = row.get('TagName')
        if(row.get('Count') != None):
            count = row.get('Count')
        id = id.encode('ascii', 'ignore').decode('ascii')
        tagName = tagName.encode('ascii', 'ignore').decode('ascii')
        count = count.encode('ascii', 'ignore').decode('ascii')
        line = id, tagName, count
        writer.writerow(line)
