# HB is inheriting from LB
# HB.breathe overrides LB.breathe
class LB(object):
    def breathe(self):
        print "I breathe"

class HB(LB):
    def breathe(self):
        # like a super call
        LB.breathe(self)
        print "Through lungs"

    def metathink(self):
        print "I think therefore I am"

# class SE(HB):
#     def code(self):
#         print "I can code"

obj = HB()
obj.breathe()
obj.metathink()

# Version 1
# class LB(object):
#     def breathe(self):
#         print "I breathe"
#
# class HB(object):
#     def breathe(self):
#         print "I breathe"

# is-a relationship question
# is LB a HB? - no
# is HB a LB? - yes