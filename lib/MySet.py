class MySet:
    
    
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

#    this method checks if the value is already
# included in the set and returns true if so .
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        # add a value as a key on the dict 
        self.dictionary[value] = True
        # return the updated set
        return self
    
    def delete(self, value):
        # delete a value from the dict
        # if value in self.dictionary:
        #     del self.dictionary[value]
        self.dictionary.pop(value, None)
        # return the updated set
        return self
    
    def size(self):
        return len(self.dictionary)
    # for removing all items in the set
    def clear(self):
        self.dictionary.clear()
        return self
    # check type of string
     
    def __str__(self):
        return f"MySet: {{{','.join(str(key) for key in self.dictionary.keys())}}}"
