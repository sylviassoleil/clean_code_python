class SomeObj:
    instance_attribute = [0]
    def __init__(self, item, name):
        self.instance_attribute.append(item)
        #equivalent SomeObj.instance_attribute.append(item)
        self.name = name # instance attributes

    @property
    def attribute_len(self):
        return len(self.instance_attribute)

    @attribute_len.setter
    def attribute_len(self, n):
        if len(self.instance_attribute)>n:
            self.instance_attribute = self.instance_attribute[:n]
        return len(self.instance_attribute)

    @attribute_len.deleter
    def attribute_len(self):
        self.instance_attribute = []

    def __getattr__(self, item):
        return self.__dict__.get(item, "hasn't been defined")

    @classmethod
    def concat_result(cls):
        # can only access class attributes, the class attributes are not accessible
        print('%s has instance_attribute of %s' %(cls.__dict__.get('name', 'has not defined'), cls.instance_attribute))
if __name__ == '__main__':
    pass
    o = SomeObj(1, 'a')
    b = SomeObj(2, 'b')
    id(o.instance_attribute) == id(b.instance_attribute) #True
    SomeObj.concat_result()


