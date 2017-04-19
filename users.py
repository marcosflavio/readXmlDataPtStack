import xml.etree.ElementTree as ET
import csv
tree = ET.parse('/home/marcos/pt stack/Users.xml')
root = tree.getroot()
count = 0
header = (
'Id', 'Reputation', 'CreationDate', 'DisplayName', 'LastAccessDate', 'WebsiteUrl', 'Location', 'AbouteMe', 'Views',
'UpVotes', 'DownVotes', 'AccountId', 'Age')

with open('/home/marcos/pt stack/usersOutput.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in root.findall('row'):
        reputation = ''
        id = ''
        creationDate = ''
        displayName = ''
        lastAccessDate = ''
        webSiteUrl = ''
        location = ''
        abouteMe = ''
        views = ''
        upvotes = ''
        downvotes = ''
        accountId = ''
        age = ''
        if(row.get('Reputation') != None):
            reputation = row.get('Reputation')
        if(row.get('Id') != None):
            id = row.get('Id')
        if(row.get('CreationDate') != None):
            creationDate = row.get('CreationDate')
        if(row.get('DisplayName')!= None):
            displayName = row.get('DisplayName')
        if(row.get('LastAccessDate') != None):
            lastAccessDate = row.get('LastAccessDate')
        if(row.get('WebsiteUrl') != None):
            webSiteUrl = row.get('WebsiteUrl')
        if(row.get('Location') != None):
            location = row.get('Location')
        if(row.get('AboutMe') != None):
            abouteMe = row.get('AboutMe')
        if(row.get('Views') != None):
            views = row.get('Views')
        if(row.get('UpVotes') != None):
            upvotes = row.get('UpVotes')
        if(row.get('DownVotes') != None):
            downvotes = row.get('DownVotes')
        if(row.get('AccountId') != None):
            accountId = row.get('AccountId')
        if(row.get('Age') != None):
            age = row.get('Age')

        id = id.encode('ascii', 'ignore').decode('ascii')
        reputation = reputation.encode('ascii', 'ignore').decode('ascii')
        creationDate = creationDate.encode('ascii', 'ignore').decode('ascii')
        displayName = displayName.encode('ascii', 'ignore').decode('ascii')
        lastAccessDate = lastAccessDate.encode('ascii', 'ignore').decode('ascii')
        webSiteUrl = webSiteUrl.encode('ascii', 'ignore').decode('ascii')
        location = location.encode('ascii', 'ignore').decode('ascii')
        abouteMe = abouteMe.encode('ascii', 'ignore').decode('ascii')
        views = views.encode('ascii', 'ignore').decode('ascii')
        upvotes = upvotes.encode('ascii', 'ignore').decode('ascii')
        downvotes = downvotes.encode('ascii', 'ignore').decode('ascii')
        accountId = accountId.encode('ascii', 'ignore').decode('ascii')
        age = age.encode('ascii', 'ignore').decode('ascii')
        line = id, reputation, creationDate, displayName, lastAccessDate, webSiteUrl, location, abouteMe, views, upvotes, downvotes, accountId, age
        writer.writerow(line)
