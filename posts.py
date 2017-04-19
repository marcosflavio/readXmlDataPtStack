import xml.etree.ElementTree as ET
import csv
tree = ET.parse('/home/marcos/pt stack/Posts.xml')
root = tree.getroot()
header = ('Id', 'PostTypeId', 'AcceptedAnswerId', 'DisplayName', 'CreationDate', 'ParentId',
           'DeletionDate', 'Score', 'ViewCount', 'Body', 'OwnerUserId',
           'LastEditorUserId', 'LastEditDate', 'LastActivityDate', 'Title', 'AnswerCount',
          'CommentCount', 'FavoriteCount', 'ClosedDate', 'Tags')

with open('/home/marcos/pt stack/postsOutput.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    id = ''
    postTypeId = ''
    accpetedAnswerId = ''
    displayName = ''
    creationDate = ''
    parentId = ''
    deletionDate = ''
    score = ''
    viewCount = ''
    body = ''
    ownerUserId = ''
    lastEditorUserId = ''
    lastEditDate = ''
    lastActivityDate = ''
    title = ''
    answerCount = ''
    commentCount = ''
    favoriteCount = ''
    closedDate = ''
    tags = ''
    for row in root.findall('row'):
        if(row.get('PostTypeId') != None):
            postTypeId = row.get('PostTypeId')
        if(row.get('Id') != None):
            id = row.get('Id')
        if(row.get('AcceptedAnswerId') != None):
            accpetedAnswerId = row.get('AcceptedAnswerId')
        if(row.get('DisplayName')!= None):
            displayName = row.get('DisplayName')
        if(row.get('CreationDate') != None):
            creationDate = row.get('CreationDate')
        if(row.get('ParentId') != None):
            parentId = row.get('ParentId')
        if(row.get('DeletionDate') != None):
            deletionDate = row.get('DeletionDate')
        if(row.get('Score') != None):
            score = row.get('Score')
        if(row.get('ViewCount') != None):
            viewCount = row.get('ViewCount')
        if(row.get('Body') != None):
            body = row.get('Body')
        if(row.get('OwnerUserId') != None):
            ownerUserId = row.get('OwnerUserId')
        if(row.get('LastEditorUserId') != None):
            lastEditorUserId = row.get('LastEditorUserId')
        if(row.get('LastEditDate') != None):
            lastEditDate = row.get('LastEditDate')
        if (row.get('LastActivityDate') != None):
            lastActivityDate = row.get('LastActivityDate')
        if (row.get('Title') != None):
            title = row.get('Title')
        if (row.get('AnswerCount') != None):
            answerCount = row.get('AnswerCount')
        if (row.get('CommentCount') != None):
            commentCount = row.get('CommentCount')
        if (row.get('FavoriteCount') != None):
            favoriteCount  = row.get('FavoriteCount')
        if (row.get('ClosedDate') != None):
            closedDate  = row.get('ClosedDate')
        if (row.get('Tags') != None):
            tags  = row.get('Tags')

        id = id.encode('ascii', 'ignore').decode('ascii')
        postTypeId = postTypeId.encode('ascii', 'ignore').decode('ascii')
        accpetedAnswerId = accpetedAnswerId.encode('ascii', 'ignore').decode('ascii')
        displayName = displayName.encode('ascii', 'ignore').decode('ascii')
        creationDate = creationDate.encode('ascii', 'ignore').decode('ascii')
        parentId = parentId.encode('ascii', 'ignore').decode('ascii')
        deletionDate = deletionDate.encode('ascii', 'ignore').decode('ascii')
        score = score.encode('ascii', 'ignore').decode('ascii')
        viewCount = viewCount.encode('ascii', 'ignore').decode('ascii')
        body = body.encode('ascii', 'ignore').decode('ascii')
        ownerUserId = ownerUserId.encode('ascii', 'ignore').decode('ascii')
        lastEditorUserId = lastEditorUserId.encode('ascii', 'ignore').decode('ascii')
        lastEditDate = lastEditDate.encode('ascii', 'ignore').decode('ascii')
        lastActivityDate = lastActivityDate.encode('ascii', 'ignore').decode('ascii')
        title = title.encode('ascii', 'ignore').decode('ascii')
        answerCount = answerCount.encode('ascii', 'ignore').decode('ascii')
        commentCount = commentCount.encode('ascii', 'ignore').decode('ascii')
        favoriteCount = favoriteCount.encode('ascii', 'ignore').decode('ascii')
        closedDate = closedDate.encode('ascii', 'ignore').decode('ascii')
        tags = tags.encode('ascii', 'ignore').decode('ascii')

        line = (id, postTypeId, accpetedAnswerId, displayName, creationDate, parentId, deletionDate, score,
                viewCount, body, ownerUserId, lastEditorUserId, lastEditDate, lastActivityDate, title,
                answerCount, commentCount, favoriteCount, closedDate, tags)
        writer.writerow(line)
