from . import CONN, CURSOR
import re

class Main:

    all = {}

    def __init__(self, name, email, id):
        self.name = name
        self.email= email
        self.id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('value name must be str')

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.fullmatch(email_pattern, value):
            self._email = value
        else:
            raise ValueError('regular expression of email`s value not in full match ')

    def __str__(self):
        return f"name:\t{self._name}\nemail:\t{self._email}"

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
            INSERT INTO users (name, email)
                VALUES (?, ?);
        """

        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        new_user = cls(name, email)
        new_user.save()
        return new_user

    def delete(self):
        sql = """
            DELETE FROM users
                WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
    
    def update(self):
        sql = """
            UPDATE users
            SET name = ? , email = ?
            WHERE id = ? ;
        """
        CURSOR.execute(sql, (self.name, self.email, self.id))
        CONN.commit()
    @classmethod
    def get_by_id(cls,id_):
        sql = """
            SELECT * FROM users WHERE id = ?;
        """
        row = CURSOR.execute(sql, (id_)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all_sub(cls):
        pass

    @classmethod
    def instance_from_db(cls, row):
        obj_instance = cls.all.get(row[0])

        if obj_instance:
            obj_instance.id = row[0]
            obj_instance.name = row[1]
            obj_instance.email = row[2]
        else:
            obj_instance = cls(row[1], row[2])
            obj_instance.id = row[0]
            cls.all[obj_instance.id] = obj_instance
        return obj_instance





if __name__ == "__main___":
    Main()
