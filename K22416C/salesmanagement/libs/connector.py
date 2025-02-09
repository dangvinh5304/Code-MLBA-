import mysql.connector
class MySQLconnector:
    def __init__(self, server = None, port = None, database = None, username = None, password = None):
        if server == None:
            self.server = "localhost"
            self.port = 3306
            self.database = "k22416c_sales"
            self.username = "root"
            self.password = "prolaner8560"
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password
    def connector(self):
        self.conn = mysql.connector.connect(
            host=self.server,
            port=self.port,
            database=self.database,
            user=self.username,
            password=self.password)
        return self.conn


