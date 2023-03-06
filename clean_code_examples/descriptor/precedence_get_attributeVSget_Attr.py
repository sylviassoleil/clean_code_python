'''
This compares __getattribute__ , __getattr__ , and getattr()

getattr(object, variable_name) is equivalent to object.variable_name
top priority: __getattribute__
this will also override the main entry for all attribute access

last: __getattr__
if __getattribute__ is not defined, will fo to this

'''


class SomeAttributes:
    def __init__(self, t):
        self.v = t

    def __getattribute__(self, item):
        '''
        first
        :param item:
        :return:
        '''
        # return self.__getattribute__(item) this would invoke the infinite loop
        # return object.__getattribute__(self, item)
        if str(item) == 'v':
            return 'redefined __getattribute__'
        else:
            return object.__getattribute__(self, item)
            # return 'redefined __getattribute__'

    def __getattr__(self, item):
        '''
        last:
        gets called if there is no attribute in the instance.
        '''
        if item =='v':
            return '%s __getattr__' % item
        else:
            return '__getattr__ undefined' # if called


if __name__ == '__main__':
    s = SomeAttributes(1)
    ''' to visit an assigned attribute '''
    s.v # call s.__getattribute__('v')
    getattr(s, 'v')

    # return 'redefined __getattribute__'

    ''' to visit an assigned attribute '''
    s.t # call __getattr__,
    # bcs object.__getattribute__(self, 't') couldn't get the attribute
    # AttributeError: 'SomeAttributes' object has no attribute 't'




