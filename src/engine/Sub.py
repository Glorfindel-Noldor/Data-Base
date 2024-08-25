#these are the logs

class Sub:

    all = {}

    def __init__(self, log, foreign_id, id):
        self.log = log
        self.foreign_id = foreign_id
        self.id = id
    
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
        pass

    @classmethod
    def create_table(cls):
        pass

    @classmethod
    def save(cls):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    @classmethod
    def get_by_id(cls):
        pass

    @classmethod
    def get_all_by_foreign_id(cls):
        pass

    @classmethod
    def instance_from_db(cls, row):
        obj_instance = cls.all.get(row[0])

        if obj_instance:
            obj_instance.id         = row[0]
            obj_instance.log        = row[1]
            obj_instance.foreign_id = row[2]

        else:
            obj_instance = cls(row[1], row[2])
            obj_instance.id = row[0]
            cls.all[obj_instance.id] = obj_instance

        return obj_instance;
