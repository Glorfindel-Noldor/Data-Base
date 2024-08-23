from . import CONN, CURSOR

class Main:
    def __init__(self, angel):
        self.angel = angel

    @property
    def angel(self):
        return self._angel
    @angel.setter
    def angel(self, value):
        if isinstance(value, str):
            self._angel = value
        else:
            raise ValueError('value angel must be str')
        

if __name__ == "__Main___":
    Main()


print('hello from Main.py !')
