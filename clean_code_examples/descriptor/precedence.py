class DataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

    def __set__(self, instance, value):
        print("setting %s.descriptor to %s" %(instance, value))
        instance.__dict__["descriptor"] = value


class ClientClass:
    descriptor = DataDescriptor()

if __name__ == '__main__':
    pass
    client = ClientClass()
    client.descriptor
    '''42'''
    vars(client)
    '''{}'''
    client.descriptor = 99
    client.descriptor
    '''42 '''
    vars(client)
    '''{'descriptor': 99}'''

    client.__dict__["descriptor"]
    '''99'''

    del client.descriptor
    ''' AttributeError: __delete__'''
    '''because, the descriptor always takes place, 
    calling del on an object doesn't try to delete the attribute from the dictionary (__dict__) of the object, 
    but instead it tries to call the __delete__() method of the descriptor (which is not implemented in this example, 
    hence the attribute error).'''


