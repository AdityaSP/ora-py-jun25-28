class A(object):
    # def f1(self):
    #     print "From A"
    pass

class B(object):
    def f1(self):
        print "From B"

class C(object):
    def f1(self):
        print "From C"

class D(C,A,B):
    pass

objd = D()
print objd.f1()

#method resolution order
print D.__mro__