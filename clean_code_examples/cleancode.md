### Extensible system 

### Good decorators 
- Encapsulation, or separation of concerns: only invoke it in black box mode
- Orthogonality: independent as possible of the object it is decorating.
- Reusability: can be applied to multiple types.

`from functools import wraps` #todo

### Descriptor 
A descriptor is, therefore, just an object that is an instance of a class that implements the descriptor protocol. This means that this class must have its interface containing at least one of the following magic methods (part of the descriptor protocol as of Python 3.6+):

**Always place the descriptor object as a class attribute!**
- `__get__`
- `__set__`
- `__delete__`
- `__set_name__`


##### `__get__(instance, owner)`

When an object is defined as a class attribute (and this one is a descriptor), 
when a client requests this attribute, 
instead of getting the object itself (as we would expect from the previous example), 
we get the result of having called the `__get__` magic method.
[demo](clean_code_examples/descriptor/descriptor_get.py)

##### `__set__(self, instance, value)` 
a descriptor is an object tht implement `__set__`,
the instance would be client 
```client.descriptor = "value"``` 

if client.descriptor doesn't implement `__set__`, then the calue will override the descriptor entirely.

By default, the most common use of this method is just to store data in an object.

for example, if we were to create generic validation objects that can be applied multiple times (again, this is something that if we don't abstract, 
we might end up repeating multiple times in setter methods of properties). [demo](clean_code_examples/descriptor/descriptor_set.py)


##### `__delete__(self, instance)`
something to note: preservation of the class attibutes:
**it was decided that the "deletion" of an email will just simply set it to None, and that is the part of the code listing that is in bold.**
[demo](clean_code_examples/descriptor/descriptor_delete.py)
so instead of delete the object's attribute, set it to None, and override the del method 
*Can protect the deletion of some attribute by restricting the permission role (value of an attribute)

##### `__set_name__(self, owner, name)`

This attribute name is the one we use to read from and write to __dict__ in the __get__ and __set__ methods, respectively.

Now, if we wanted to avoid writing the name of the attribute twice (once for the variable assigned inside the class, and once again as the name of the first parameter of the descriptor), we have to resort to a few tricks, like using a class decorator, or (even worse) using a metaclass.
In Python 3.6, the new method `__set_name__` was added, and it receives the class where that descriptor is being created, and the name that is being given to that descriptor. The most common idiom is to use this method for the descriptor so that it can store the required name in this method.
[demo](clean_code_examples/descriptor/descriptor_set_name.py)

For compatibility, it is generally a good idea to keep a default value in the __init__ method but still take advantage of `__set_name__`.


### Types of descriptors
| Type                    | Descriptors             |
|:------------------------|:------------------------|
| **data descriptor**     | `__set__`, `__delete__` |
| **non-data descriptor** | `__get__`                |
 `__set_name__` does not affect this classification
**Precedence**: data-descriptor --> non-data descriptor

if the descriptor implements `__set__()`, then it will always take precedence, no matter whar attributes are present in the dictionary of the object

if the method is not implememted, then the dictionary will be searched first, then the descriptor will run.

#### flag
Do not use `setattr()` or the assignment expression directly on the descriptor inside the `__set__` method because that will trigger an infinite recursion.

