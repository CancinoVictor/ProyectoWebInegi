from .Database import Database

class CRUD:
    def __init__(self, table_name, primary_key, auto_increment=False):
        self.table_name = table_name
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.db = Database()

    def create(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        values_template = ', '.join(['%s'] * len(kwargs))
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values_template})"
        values = tuple(kwargs.values())

        conn = self.db.conn
        cursor = self.db.cursor

        try:
            cursor.execute(query, values)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            pass

    def read(self, **kwargs):
        conditions = ' AND '.join([f"{key} = %s" for key in kwargs.keys()])
        query = f"SELECT * FROM {self.table_name} WHERE {conditions}"
        values = tuple(kwargs.values())

        conn = self.db.conn
        cursor = self.db.cursor

        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            pass

    def update(self, primary_value, **kwargs):
        set_clause = ', '.join([f"{key} = %s" for key in kwargs.keys()])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {self.primary_key} = %s"
        values = tuple(kwargs.values()) + (primary_value,)

        conn = self.db.conn
        cursor = self.db.cursor

        try:
            cursor.execute(query, values)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            pass

    def delete(self, primary_value):
        query = f"DELETE FROM {self.table_name} WHERE {self.primary_key} = %s"

        conn = self.db.conn
        cursor = self.db.cursor

        try:
            cursor.execute(query, (primary_value,))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            pass

        # Si el valor es autoincremental, resetear el contador de autoincremento
        if self.auto_increment:
            self.reset_auto_increment()

    def reset_auto_increment(self):
        # Resetear el contador de autoincremento
        query = f"ALTER TABLE {self.table_name} AUTO_INCREMENT = 1"

        conn = self.db.conn
        cursor = self.db.cursor

        try:
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            pass
