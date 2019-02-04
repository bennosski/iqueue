
class iqueue:

    def __init__(self, iterable=[]):
        '''
        constructs new iqueue object

        - values : may be a list of values with which to initialize the iqueue
        '''
        self._shift = 0
        self._map = {i:v for i,v in enumerate(iterable)}

    def append(self, v):
        self._map[len(self._map)+self._shift] = v

    def appendleft(self, v):
        self._shift -= 1
        self._map[self._shift] = v

    #def clear():
    #    self([])

    #def copy():
    #    pass

    #def count():

    #def extend(iterable):

    #def extendleft(iterable):

    #def index(x[, start[, stop]])

    #def insert(i,x):
       # will be inefficient
    
    def pop(self):
        v = self._map[len(self._map)-1+self._shift]
        del self._map[len(self._map)-1+self._shift]
        return v
        
    def popleft(self):
        v = self._map[self._shift]
        del self._map[self._shift]
        self._shift += 1
        return v

    # def remove(v):

    # def rotate(n=1):
    
    def __getitem__(self, i):
        return self._map[i+self._shift]

    def __setitem__(self, i, v):
        self._map[i+self._shift] = v

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i<len(self._map):
            r = self[self.i]
            self.i += 1
            return r
        else:
            raise StopIteration

    def __bool__(self):
        return len(self._map)>0

    def __len__(self):
        return len(self._map)
    
    def __str__(self):
        return [self.__getitem__(i) for i in range(len(self._map))].__str__()

        


    

        
        
