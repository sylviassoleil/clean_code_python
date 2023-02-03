
class DescriptorClass:
    def __get__(self, instance, owner):
        '''

        :param instance: the object from what descriptor is called, <__main__.ClientClass object at 0x7fe6283e6740>
        :param owner:  <class '__main__.ClientClass'>
        :return:
        '''
        if instance is None:
            return self
        print("Call: %s.__get__(%r, %r)" % (self.__class__.__name__, instance, owner))
        return instance

class ClientClass:
    descriptor = DescriptorClass()

''' 
When an object is defined as a class attribute (and this one is a descriptor), 
when a client requests this attribute, instead of getting the object itself (as we would expect from the previous example), 
we get the result of having called the __get__ magic method.

'''
if __name__ == '__main__':
    # 1
    client = ClientClass()
    client.descriptor is client
    ''' output 
    Call: DescriptorClass.__get__(<__main__.ClientClass object at 0x7fe6283e6740>, <class '__main__.ClientClass'>)
    True
    '''
    # 2
    ClientClass().descriptor is client
    ''' output
    Call: DescriptorClass.__get__(<__main__.ClientClass object at 0x7fe6283e6a70>, <class '__main__.ClientClass'>)
    False
    '''
    d = ClientClass.descriptor
    #in general, the most common idiom, is to just return the descriptor itself, when instance is None
    ''' output 
    <__main__.DescriptorClass object at 0x7fe6283e5d50>
    '''



