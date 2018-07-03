import core.bank

sa = core.bank.SA('Aditya')
print sa.n, sa.b, sa.t
try:
    sa.debit(2000)
except core.bank.InsufficientBalanceError as ibe:
    print "Please check your balance and retry"

ca = core.bank.CA('ABC Pvt Ltd')
print ca.n, ca.b, ca.t


#Version 1
# import core.bank
#
# ac = core.bank.Account('Aditya')
# print type(ac)
# print ac.n, ac.b, ac.t
#
# ac.debit(100)
# print ac.n, ac.b, ac.t
#
# ac.credit(1000000)
# print ac.n, ac.b, ac.t
