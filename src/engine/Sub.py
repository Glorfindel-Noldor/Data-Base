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
    def instance_from_db(cls):
        pass
