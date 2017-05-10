class FooClass(object):
    'my very first class: FooClass'
    version = 0.1   # class (data) attribute
    def __init__(self, nm='John Doe'):
        'constructor'
        self.name = nm # class instance (data) attibute
        print 'Create a class instance for', nm
    def showname(self):
        'Display instance attibute and class name'
        print 'Your name is', self.name
        print 'My name is', self.__class__.__name__
    def showver(self):
        'Display class (static) attibute'
        print self.version # reference FooClass.version
    def addMe2Me(self, x):
        'Apply + opration to argument'
        return x + x
