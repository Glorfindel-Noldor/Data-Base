from . import CONN, CURSOR

class Sub:

    all = {}

    def __init__(self, id, log, foreign_id = None):
        self.id = id
        self.log = log
        self.foreign_id = foreign_id
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if value is None or isinstance(value, int):
            self._id = value
        else:
            raise ValueError(f'value must be in int form instead got: {type(value)}')


    @property
    def log(self):
        return self._log
    
    @log.setter
    def log(self, value):
        self._log = value
    
    @property
    def foreign_id(self):
        return self._foreign_id
    
    @foreign_id.setter
    def foreign_id(self, value):
        if isinstance(value, int):
            self._foreign_id = value
        else:
            raise ValueError('foreign id should be int value')
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS logs;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log TEXT,
                foreign_id INTEGER,
                FOREIGN KEY(foreign_id) REFERENCES users(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO logs (log, foreign_id)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.log, self.foreign_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, log, foreign_id):
        new_log = cls(None, log, foreign_id)
        new_log.save()
        return new_log

    def delete(self):
        sql = """
            DELETE FROM logs
                WHERE id = ? ;
        """
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()
        del type(self).all[self.id]

    def update(self):
        sql = """
            UPDATE logs
            SET log = ?  
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.log, self.id))

    @classmethod
    def get_by_id(cls, id):
        sql = """
            SELECT * FROM logs WHERE id = ? ;
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all_by_foreign_id(cls, foreign_id):
        sql = """
            SELECT * FROM logs WHERE foreign_id = ? ;
        """
        try:
            rows = CURSOR.execute(sql, (foreign_id, )).fetchall()
            return [cls.instance_from_db(row) for row in rows]
        except:
            return []


    @classmethod
    def instance_from_db(cls, row):
        obj_instance = cls.all.get(row[0])

        if obj_instance:
            obj_instance.id         = row[0]
            obj_instance.log        = row[1]
            obj_instance.foreign_id = row[2]

        else:
            obj_instance = cls(row[0], row[1], row[2])
            cls.all[obj_instance.id] = obj_instance

        return obj_instance;

