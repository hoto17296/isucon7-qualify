import MySQLdb
import MySQLdb.cursors

dsn = {
    'host': '192.168.33.13',
    'port': 3306,
    'user': 'isucon',
    'password': 'isucon',
    'database': 'isubata',
    'cursorclass': MySQLdb.cursors.SSCursor,
}

conn = MySQLdb.connect(**dsn)
cur = conn.cursor()
cur.execute('SELECT DISTINCT name, data FROM image')
for name, data in cur:
    with open('/home/isucon/image/icons/{}'.format(name), 'wb') as f:
        f.write(data)
cur.close()
conn.close()
