
# Todo:
#
# - implement insert(i, v) function
# - add documentation of all methods with examples
# - optimization :
#        for __delitem__, remove, rotate, and insert consider the cases when i<N//2 versus i>N//2 separately
#

class iqueue:

    def __init__(self, iterable=[]):
        '''
        constructs new iqueue object

        - values : may be a list of values with which to initialize the iqueue
        '''
        self._shift = 0
        self._map = {i:v for i,v in enumerate(iterable)}

    def append(self, v):
        '''
        Add x to the right side of the iqueue.
        O(1)
        '''
        self._map[len(self._map)+self._shift] = v

    def appendleft(self, v):
        '''
        Add x to the left side of the iqueue.
        O(1)
        '''
        self._shift -= 1
        self._map[self._shift] = v

    def clear(self):
        '''
        Remove all elements form the iqueue leaving it with length 0.
        '''
        self.__init__([])

    def count(self, x):
        '''
        Count the number of iqueue elements equal to x.
        O(n)
        '''
        return list(self._map.values()).count(x)
    
    def extend(self, iterable):
        '''
        Extend the right side of the iqueue by appending elments for the iberable argument.
        O(k)
        '''
        for x in iterable:
            self.append(x)
        
    def extendleft(self, iterable):
        '''
        Extend the left side of the iqueue by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.
        O(k)
        '''
        for x in iterable:
            self.appendleft(x)
        
    def pop(self):
        '''
        Remove and return an element from the right side of the iqueue. If no elements are present, raises and IndexError.
        O(1)
        '''
        if not self.__bool__():
            raise IndexError
        v = self._map[len(self._map)-1+self._shift]
        del self._map[len(self._map)-1+self._shift]
        return v
        
    def popleft(self):
        '''
        Remove and return an element from the left side of the iqueue. If no elements are present, raises and IndexError.
        O(1)
        '''
        if not self.__bool__():
            raise IndexError
        v = self._map[self._shift]
        del self._map[self._shift]
        self._shift += 1
        return v

    def remove(self, v):
        ''' 
        Remove the first occurence of value. If not found, raises a ValueError
        O(n)
        '''
        found = False
        i = 0
        L = len(self._map)
        while i < L:
            if self[i]==v:
                found = True
                break
            i += 1

        if not found:
            raise ValueError
            
        while i < L-1:
            self[i] = self[i+1]
            i += 1
            
        del self._map[L-1+self._shift]

    #def insert(self, i, v):
    #    pass
        
    def rotate(self, n=1):
        '''
        Rotate the iqueue n steps to the right. If n is negative, rotate to the left.

        When the iqueue is not empty, rotating one step to the right is equivalent to iq.appendleft(iq.pop()), and rotating one step to the left is equivalent to iq.append(iq.popleft()).
        O(k)
        '''
        if n>0:
            for _ in range(abs(n)): self.appendleft(self.pop())
        else:
            for _ in range(abs(n)): self.append(self.popleft())
        
    def __getitem__(self, i):
        ''' 
        O(1)
        '''
        return self._map[i+self._shift]

    def __setitem__(self, i, v):
        ''' 
        O(1)
        '''
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

    def __delitem__(self, i):
        ''' 
        Delete the element at index i. If index out of range, raises and IndexError.
        O(n)
        '''

        if i<0 and abs(i)>len(self._map):
            raise IndexError
        if i>=0 and abs(i)>=len(self._map):
            raise IndexError

        if i<0:
            i = len(self._map)+i
        
        if i==0:
            self.popleft()
        else:
            while i < len(self._map)-1:
                self[i] = self[i+1]
                i += 1
            del self._map[len(self._map)-1+self._shift]
            
    def __bool__(self):
        return len(self._map)>0

    def __len__(self):
        return len(self._map)
    
    def __str__(self):
        return [self[i] for i in range(len(self._map))].__str__()

    def __repr__(self):
        return 'iqueue({})'.format(self.__str__())


    

        
        
