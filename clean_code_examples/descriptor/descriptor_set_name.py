import logging
class DescriptorClassWithName:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        '''

        :param instance: the object from what descriptor is called, <__main__.ClientClass object at 0x7fe6283e6740>
        :param owner:  <class '__main__.ClientClass'>
        :return:
        '''
        if instance is None:
            return self
        print("getting %s attribute from %s" % (self.name, instance))
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        '''
        it receives the class where that descriptor is being created,
        and the name that is being given to that descriptor.
        The most common idiom is to use this method for the descriptor so that it can store the required name in this method.
        :param owner:
        :param name:
        :return:
        '''
        self.name = name

class ClientClass:
    descriptor = DescriptorClassWithName("descriptor")

if __name__ == '__main__':
    # 1
    logger = logging.getLogger('info')
    logger.setLevel('INFO')
    client = ClientClass()
    client.descriptor = 'test'
