#test.py

class BadDataError(Exception):
    """docstring for BadDataError"""
    ID = 0

    def __init__(self, *args):
        super(BadDataError, self).__init__(args)
        BadDataError.ID += 1
        self.ID = BadDataError.ID
        
