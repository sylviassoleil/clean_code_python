metaclass allows customization of class instantiation.
[Examples](metaclass_example.py)

This can also be done with simple inheritance 
```
class Base:
    attr = 100

class X(Base):
    pass      
```

or class Decorator 

``` 
def decorator(cls):
    class NewClass(cls):
        attr = 100 
    return NewClass 

@decorator
class X:
    pass 
```

for Python > 3, type(obj) is the same is `obj.__class__`)

``` 
class Foo:
    pass

x = Foo() 
n = 5 
d = {'s':1}

for obj in (n, d, x):
    print(type(obj) is obj.__class__)

True
True
True
```
`type(obj) is obj.__class__`  type and `__class__` is interchangeable

`type(Foo)` `<class 'type'>`\
`type(obj)` `<class '__main__.Foo'>`

- `type` is immutable 
`type.__new__ = some_func()` will raise a TypeError
`TypeError: cannot set '__new__' attribute of immutable type 'type'`


