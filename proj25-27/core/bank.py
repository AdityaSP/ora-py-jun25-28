class InsufficientBalanceError(Exception):
    pass
class Account(object):
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def debit(self, amount):
        self.b -= amount
    def credit(self, amount):
        self.b += amount
class SA(Account):
    def __init__(self, n, b=1000):
        Account.__init__(self, n, b,'S')
    def debit(self,amount):
        if self.b > amount:
            Account.debit(self,amount)
        else:
            raise InsufficientBalanceError(str(self.b))
class CA(Account):
    def __init__(self, n, b=0):
        Account.__init__(self,n,b,'C')



# SA => not debit more than what exists
# CA => can debit more than what exists
#version 4
# class Account(object):
#     def __init__(self, n, b, t):
#         self.n = n
#         self.b = b
#         self.t = t
#
#     def debit(self, amount):
#         self.b -= amount
#     def credit(self, amount):
#         self.b += amount
#
# class SA(Account):
#     def __init__(self, n, b=1000):
#         Account.__init__(self, n, b,'S')
#
# class CA(Account):
#     def __init__(self, n, b=0):
#         Account.__init__(self,n,b,'C')


#Version 3
# # is SA a CA? no
# # is CA a SA? no
# # is SA an Account? yes
# # is CA an Account? yes
# class Account(object):
#     def debit(self, amount):
#         self.b -= amount
#     def credit(self, amount):
#         self.b += amount
#
# class SA(Account):
#     def __init__(self, n, b=1000):
#         self.n = n
#         self.b = b
#         self.t = 'S'
#
# class CA(Account):
#     def __init__(self, n, b=0):
#         self.n = n
#         self.b = b
#         self.t = 'C'

# Version 2
# # repetition => maintenance,
# class SA(object):
#     def __init__(self, n, b=1000):
#         self.n = n
#         self.b = b
#         self.t = 'S'
#     def debit(self, amount):
#         self.b -= amount
#     def credit(self, amount):
#         self.b += amount
#
# class CA(object):
#     def __init__(self, n, b=0):
#         self.n = n
#         self.b = b
#         self.t = 'C'
#     def debit(self, amount):
#         self.b -= amount
#     def credit(self, amount):
#         self.b += amount


                #Version 1
# class Account(object):
#     # loosely referred as constructor
#     def __init__(self, n, b=1000, t='S'):
#         # n,b,t => data members
#         self.n = n
#         self.b = b
#         self.t = t
#     # debit, credit => methods or behaviour
#     def debit(self, amount):
#         self.b -= amount
#     def credit(self, amount):
#         self.b += amount
#     # together n,b,t,debit,credit => attributes of the class
#     # Encapsulation => putting data and behaviour together