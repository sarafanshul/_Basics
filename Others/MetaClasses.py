class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class S:
    pass

class A(S, metaclass=LittleMeta):
    pass

a = A()
#We can see LittleMeta.__new__ has been called and not type.__new__.
