import ipdb
from src.engine.Main import Main
from src.engine.Sub import Sub

def debug():
    try:
        Main.drop_table()
        Sub.drop_table()
        Main.create_table()
        Sub.create_table()
        print('table set')
        ipdb.set_trace()
    except:
        raise ValueError('tables not created and failed to debug')


debug()