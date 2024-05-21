import pymysql

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            try:
                self.conn = pymysql.connect(host='localhost',
                                            port=3306,
                                            user='cancino',
                                            passwd='root',
                                            db='censo')
                self.cursor = self.conn.cursor()
                self.__initialized = True
                print("Database connection successful.")
            except Exception as e:
                print("Error connecting to database:", e)

    def close(self):
        pass  # Don't close the connection

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error executing query:", e)
            return False

    def fetch_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching data:", e)
            return None
