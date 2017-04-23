import xml.etree.ElementTree as ET
#import csv
import unicodecsv as csv
#tree = ET.parse('/home/marcos/pt stack/Posts.xml')
#root = tree.getroot()
header = ('Id', 'PostTypeId', 'AcceptedAnswerId', 'CreationDate', 'ParentId', 'Score', 'Body', 'OwnerUserId',
            'Title', 'FavoriteCount', 'Tags')

with open('/home/marcos/pt stack/Posts.xml', 'r') as o:
    tree = ET.parse(o)
    root = tree.getroot()

with open('/home/marcos/pt stack/postsOutputNew.csv', 'w') as f:
    writer = csv.writer(f, encoding='utf-8')
    writer.writerow(header)
    for row in root.findall('row'):
        id = ''
        postTypeId = ''
        accpetedAnswerId = '0'
        # displayName = ''
        creationDate = ''
        parentId = '0'
        # deletionDate = ''
        score = '0'
        # viewCount = ''
        body = ''
        ownerUserId = '0'
        # lastEditorUserId = ''
        # lastEditDate = ''
        # lastActivityDate = ''
        title = 'None'
        # answerCount = ''
        # commentCount = ''
        favoriteCount = '0'
        # closedDate = ''
        tags = 'None'

        if(row.get('PostTypeId') != None):
            postTypeId = row.get('PostTypeId')
        if(row.get('Id') != None):
            id = row.get('Id')
        if(row.get('AcceptedAnswerId') != None):
            accpetedAnswerId = row.get('AcceptedAnswerId')
        #if(row.get('DisplayName')!= None):
            #displayName = row.get('DisplayName')
        if(row.get('CreationDate') != None):
            creationDate = row.get('CreationDate')
        if(row.get('ParentId') != None):
            parentId = row.get('ParentId')
        #if(row.get('DeletionDate') != None):
            #deletionDate = row.get('DeletionDate')
        if(row.get('Score') != None):
            score = row.get('Score')
        #if(row.get('ViewCount') != None):
            #viewCount = row.get('ViewCount')
        if(row.get('Body') != None):
            body = row.get('Body')
        if(row.get('OwnerUserId') != None):
            ownerUserId = row.get('OwnerUserId')
        #if(row.get('LastEditorUserId') != None):
            #lastEditorUserId = row.get('LastEditorUserId')
        #if(row.get('LastEditDate') != None):
            #lastEditDate = row.get('LastEditDate')
        #if (row.get('LastActivityDate') != None):
            #lastActivityDate = row.get('LastActivityDate')
        if (row.get('Title') != None):
            title = row.get('Title')
        #if (row.get('AnswerCount') != None):
            #answerCount = row.get('AnswerCount')
        #if (row.get('CommentCount') != None):
            #commentCount = row.get('CommentCount')
        if (row.get('FavoriteCount') != None):
            favoriteCount  = row.get('FavoriteCount')
        #if (row.get('ClosedDate') != None):
            #closedDate  = row.get('ClosedDate')
        if (row.get('Tags') != None):
            tags = row.get('Tags')

        id = id.encode('ascii', 'ignore').decode('ascii')
        postTypeId = postTypeId.encode('ascii', 'ignore').decode('ascii')
        accpetedAnswerId = accpetedAnswerId.encode('ascii', 'ignore').decode('ascii')
        #displayName = displayName.encode('ascii', 'ignore').decode('ascii')
        creationDate = creationDate.encode('ascii', 'ignore').decode('ascii')
        parentId = parentId.encode('ascii', 'ignore').decode('ascii')
        #deletionDate = deletionDate.encode('ascii', 'ignore').decode('ascii')
        score = score.encode('ascii', 'ignore').decode('ascii')
        #viewCount = viewCount.encode('ascii', 'ignore').decode('ascii')
        body = body.encode('utf-8', 'ignore').decode('utf-8')
        ownerUserId = ownerUserId.encode('ascii', 'ignore').decode('ascii')
        #lastEditorUserId = lastEditorUserId.encode('ascii', 'ignore').decode('ascii')
        #lastEditDate = lastEditDate.encode('ascii', 'ignore').decode('ascii')
        #lastActivityDate = lastActivityDate.encode('ascii', 'ignore').decode('ascii')
        title = title.encode('utf-8', 'ignore').decode('utf-8')
        #answerCount = answerCount.encode('ascii', 'ignore').decode('ascii')
        #commentCount = commentCount.encode('ascii', 'ignore').decode('ascii')
        favoriteCount = favoriteCount.encode('ascii', 'ignore').decode('ascii')
        #closedDate = closedDate.encode('ascii', 'ignore').decode('ascii')
        tags = tags.encode('ascii', 'ignore').decode('ascii')
        line = (id, postTypeId, accpetedAnswerId, creationDate, parentId, score,
                 body, ownerUserId, title, favoriteCount, tags)
        writer.writerow(line)
