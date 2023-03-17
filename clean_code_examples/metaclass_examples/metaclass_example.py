import abc


class MyMeta:
    pass


''' type(MyMeta) is type '''


class MyMetaType(type):
    pass


''' type(MyMetaType) is type '''


class MyClass(metaclass=MyMeta):
    pass


Bar = type('Bar', (MyMeta,), dict(attr=100))


# equivalent to
class Bar(MyMeta):
    attr = 100


x = Bar()
x.attr  # 100
x.__class__  # <class '__main__.Bar'>
x.__class__.__bases__  # (<class '__main__.MyMeta'>,)

Foo = type('Foo',
           (),
           {'attr': 100,
            'attr_val': lambda x: x.attr})
x = Foo()
x.attr  # 100
x.attr_val() #100


def f(obj):
    print(obj.attr)

class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x
class Foo(metaclass=Meta):
    pass

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


if __name__ == '__main__':
    pass
