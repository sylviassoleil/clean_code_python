### Contents  
- [Class attributes v.s. Instance attributes](class_instance_attributes.py)
  - class decorators
    - @classmethod so that the method can be called with `ClassName.MethodName()`
      - the first argument must be `cls`, only class attributes are accessible to a claassmethod 
    - @property conjunction with `property.setter` (can set up the format check) & `property.deleter` 
- [Object creation & Value assignment](id_of_instance.py)
  - id of the objects and chain assignment
  - garbage collection
- [Circular import](class_instance_scope.py)


### [Types of attributes](class_instance_attributes.py) 
| differences          | Class Attributes                                                   | Instance Attributes                                                         |
|:---------------------|:-------------------------------------------------------------------|:----------------------------------------------------------------------------|
| **creation**         | directly inside a class                                            | inside a constructor using self parameter                                   |
| **scope**            | shared across all objects                                          | specific to object                                                          |
| **access**           | classname.class_attribute, object.class_attribute                  | object.instance_attribute                                                   |
| **value assignment** | classname.class_attribute = value will be reflected to all objects | changing value of instance attribute will not be reflected to other objects |

### [classmethod v.s. staticmethod](class_instance_attributes.py) 
| differences              | @classmethod                                                                   | @staticmethod                                                               |
|:-------------------------|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------|
| **invoke**               | ClassName.MethodName() or obj.MethodName()                                     | ClassName.MethodName() or obj.MethodName()|
| **access to attributes** | only class attributes, not instance attributes                                 | can't access any attributes                                                 |
| **write to class**       | can be used to declare a factory method that returns the objects of the class  | changing value of instance attribute will not be reflected to other objects |

