
users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    fCount=0
    for f in friendship:
        if(f[0]==user["id"] or f[1]==user["id"]): fCount+=1
    return fCount
    
def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    userDict={}
    for user in users:
        userCount=num_friends(user)
        userDict[user["name"]]=userCount
    sortedUsers=sorted(userDict.items(), key= lambda x: x[1], reverse=True)
    for user in sortedUsers:
        print("%s has %d friends" % (user[0],user[1]))
    
sort_by_num_friends()
