import MySQLdb
db = MySQL.connect(host='your host name',
    # your host is more than often localhost
                  user='your username'
                  passwd='your password'
                  db='your dataset')
                  
cur = db.cursor()
cur.execute('SELECT * FROM your table')

for row in cur.fetchall():
    print row

db.close()
