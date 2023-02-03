class Validation:
    def __init__(self, validation_function, error_msg: str):
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")


class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations


    def __set_name__(self, owner, name):
        self._name = name


    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]


    def validate(self, value):
        for validation in self.validations:
            validation(value)


    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
   descriptor = Field(
       Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
       Validation(lambda x: x >= 0, "is not >= 0"),
)

''' the ususal practice of using the equivalent of __set__. is to abstract it into a @property.setter, 
the example can be as below '''
# Python program showing the use of
# @property

class PropertySetter:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


if __name__ == '__main__':
    client = ClientClass()
    # an example to validate the data type of assigned value
    client.descriptor = 42
    print(client.descriptor) #42
    client.descriptor = -42

    ''' The idea is that something that we would normally place in a property can be abstracted away into a descriptor, 
    and reuse it multiple times. In this case, the __set__() method would be doing what the @property.setter would have been doing.
    '''

    ''' output 
    Call: DescriptorClass.__get__(<__main__.ClientClass object at 0x7fe6283e6740>, <class '__main__.ClientClass'>)
    True
    '''

