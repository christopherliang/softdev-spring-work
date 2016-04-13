import sqlite3

#+=====++ Setup ++=====+#
def setup():
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE accounts (uname text, pword text, first text, last text, info text, piclink text, friends text)")
    c.execute("CREATE TABLE posts (id integer, uname text, title text, sub text, post text, time text)")
    c.execute("CREATE TABLE comments (id integer, uname text, comment text, time text)")
    c.execute("CREATE TABLE likes (id integer, uname text)")
    conn.commit()

#+=====++ Apostrophes ++=====+#
def replaceAp(s):
    return s.replace("'", "&#8217")
def unreplace(s):
    return s.replace("&#8217", "'")
def listRep(l):
    n = []
    for s in l:
        n.append(unreplace(s))
    return n
#+=====++ Accounts ++=====+#
def unameAuth(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    accounts = c.execute("SELECT uname FROM accounts")
    for r in accounts:
        if r[0] == uname:
            return True
    return False

def pwordAuth(uname, pword):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    p = c.execute("SELECT pword FROM accounts WHERE uname = '"+uname+"';")
    for r in p:
        return r[0] == pword
    return False

def addAccount(uname, pword, first, last):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    if uname.find(",") != -1: # it can't have a comma in it
        return "This account name has a character that is not allowed (',')"
    if uname.find("'") != -1: # it can't have an apostrophe in it
        return "This account name has a character that is not allowed (''')"
    accounts = c.execute("SELECT uname FROM accounts")
    for r in accounts:
        if r[0] == uname:
            return "This account name already exists"
    c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?);", (replaceAp(uname), replaceAp(pword), replaceAp(first), replaceAp(last), "", "", ""))
    conn.commit()

def changePword(uname, oldP, newP, cNewP):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    p = c.execute("SELECT pword FROM accounts WHERE uname = '"+uname+"';")
    for r in p:
        result = r[0]
    if result != oldP:
        return "The password you input was incorrect."
    if newP != cNewP:
        return "The confirmed new password did not match."
    else:
        c.execute("UPDATE accounts SET pword = '"+replaceAp(newP)+"' WHERE uname = '"+uname+"';")
        conn.commit()        
        return "Password successfully updated"

def findName(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT first, last FROM accounts WHERE uname ='"+uname+"';")
    for r in n:
        return unreplace(r[0]+" "+r[1])

def editInfo(uname, info):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("UPDATE accounts SET info = '"+replaceAp(info)+"' WHERE uname = '"+uname+"';")
    conn.commit()

def showInfo(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT info FROM accounts WHERE uname = '"+uname+"';")
    for r in n:
        return unreplace(r[0])

def newPic(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("UPDATE accounts SET piclink = 'static/"+uname+".png' WHERE uname = '"+uname+"';")
    conn.commit()

def findPic(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT piclink FROM accounts WHERE uname = '"+uname+"';")
    for r in n:
        return r[0]
#+=====++ Friends ++=====+#
def friendList(uname): # returns list of friends
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT friends FROM accounts WHERE uname = '"+uname+"';")
    for r in n:
        return r[0].split(",") # this is why no commas!
        
def isFriend(uname, friend): # returns if uname has friend as friend
    f = friendList(uname)
    if f != None:
        for s in f:
            if s == friend:
                return True
    return False

def addFriend(uname, friend): # adds friend to uname's friends
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    if isFriend(uname, friend):
        return False
    if not unameAuth(friend):
        return False
    if not unameAuth(uname):
        return False
    f = c.execute("SELECT friends FROM accounts WHERE uname = '"+uname+"';")
    friends = ""
    for s in f:
        friends = s[0]
    if friends != "":
        friends += ","
    friends += friend
    c.execute("UPDATE accounts SET friends = '"+friends+"' WHERE uname = '"+uname+"';")
    conn.commit()
    return True
#+=====++ Blog Posts ++=====+#

# posts:
# (id, uname, post, title, sub, time)
# 
# comments:
# (id, uname, comment, time)
#
# likes:
# (id, uname)

def findID():
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    ids = c.execute("SELECT id FROM posts")
    max = 0
    for r in ids:
        id = r[0]
        if (id > max):
            max = id
    return max+1

def addPost(uname, title, sub, post):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?);", (findID(), uname, replaceAp(title), replaceAp(sub), replaceAp(post), displayDate()))
    conn.commit()

def showPosts(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    posts = c.execute("SELECT id, title, sub, post, time FROM posts WHERE uname = '"+uname+"';")
    list = []
    for r in posts:
        list.append(r)# ID, title, sub, post, stamp
    return list
def showFriendPosts(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    posts = c.execute("SELECT id, uname, title, sub, post, time FROM posts")
    friendPosts = []
    for r in posts:
        if isFriend(uname, r[1]):
            friendPosts.append(r)# note that everything after id is +1 in index
    return friendPosts

def showPost(ID):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    post = c.execute("SELECT post FROM posts WHERE id = "+str(ID)+";")
    for r in post:
        return unreplace(r[0])

def addComment(ID, uname, comment):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO comments VALUES (?, ?, ?, ?);", (ID, uname, replaceAp(comment), displayDate()))
    conn.commit()

def showComments(ID):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    comments = c.execute("SELECT uname, comment, time FROM comments WHERE id = "+str(ID)+";")
    list = []
    for r in comments:
        list.append(r)# uname, comment, time
    return list

def showAllComments():
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    comments = c.execute("SELECT id, uname, comment, time FROM comments;")
    list = []
    for r in comments:
        list.append(r)# id, uname, comment, time
    return list

def addLike(ID, uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO likes VALUES (?, ?);", (ID, uname))
    conn.commit()

def showLikes(ID):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    likes = c.execute("SELECT uname FROM likes WHERE id = "+str(ID)+";")
    list = []
    for r in likes:
        list.append(r[0])# uname
    return list

def displayDate():
    import datetime
    d = str(datetime.datetime.now())
    d = d.split(" ")
    date = ""

    time = d[1].split(":")
    day = d[0].split("-")
    
    date += day[1]+"/"+day[2]+"/"+day[0]+" at "
    date += time[0]+":"+time[1]
    return date
