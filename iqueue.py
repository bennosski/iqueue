
class node:
    def __init__(self, value):
        self.value = value
    
class iqueue:

    def __init__(self, values=[]):
        '''
        constructs new iqueue object

        - values : may be a list of values with which to initialize the iqueue
        '''

        self._shift = 0
        self._map = {i:node(v) for i,v in enumerate(values)}

    def append(self, v):
        self._map[len(self._map)+self._shift] = node(v)

    def prepend(self, v):
        self._shift -= 1
        self._map[self._shift] = node(v)

    def pop_end(self):
        v = self._map[len(self._map)+self._shift].value
        del self._map[len(self._map)+self._shift]
        return v
        
    def pop_front(self):
        v = self._map[self._shift].value
        del self._map[self._shift]
        self._shift += 1
        return v
        
    def __getitem__(self, i):
        return self._map[i+self._shift].value

    def __setitem__(self, i, v):
        self._map[i+self._shift] = node(v)

    def __iter__(self):
        pass

    def __bool__(self):
        return len(self._map)>0

    def __len__(self):
        return len(self._map)
    
    def __str__(self):
        return [self.__getitem__(i) for i in range(len(self._map))].__str__()

        


    

        
        
