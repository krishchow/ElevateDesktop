import sqlite3

class DBManager():
    def __init__(self):
        self.conn = sqlite3.connect(r'data.db')
        self.cur = self.conn.cursor()

    def CreateTables(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS auth (username, salt, saltedhash,id);')
        self.cur.execute('CREATE TABLE IF NOT EXISTS platformLogins (username, password,platformID,id);')

    def addAccount(self,table,*args):
        authStr = ''
        Arg = list(args)
        for i in range(len(Arg)):
            if i != len(Arg)-1:
                authStr += '"{' + str(i) + '}",'
            else:
                authStr += '"{' + str(i) + '}"'
        self.cur.execute('INSERT INTO {0} VALUES ({1});'.format(table,authStr).format(*args))
        self.conn.commit()

    def commit(self):
        self.conn.commit()