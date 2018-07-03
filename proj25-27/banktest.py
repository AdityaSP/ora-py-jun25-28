import HtmlTestRunner
import unittest
import core.bank as cb
import sys

class TestBank(unittest.TestCase):
    def test_sa(self):
        sa = cb.SA('Aditya')
        assert sa.b == 1000

    def test_ca(self):
        sa = cb.CA('ABC Ltd')
        assert sa.b == 0

    def test_sa_credit(self):
        sa = cb.SA('Aditya')
        sa.credit(100)
        assert sa.b == 1100

    def test_ca_credit(self):
        sa = cb.CA('ABC Ltd')
        sa.credit(100)
        assert sa.b == 10

ts = unittest.TestSuite()
#r = unittest.TextTestRunner(verbosity=3)
r = HtmlTestRunner.HTMLTestRunner(output='bank_report')

if sys.argv[1] == 'ca':
    ts.addTest(TestBank('test_ca'))
    ts.addTest(TestBank('test_ca_credit'))
    r.run(ts)
elif sys.argv[1] == 'sa':
    ts.addTest(TestBank('test_sa'))
    ts.addTest(TestBank('test_sa_credit'))
    r.run(ts)
elif sys.argv[1] == 'all':
    sys.argv = sys.argv[:1]
    unittest.main(verbosity=3, testRunner=r)
else:
    print "Not a valid test suite"

#Version 3
# import unittest
# import core.bank as cb
# import sys
#
# class TestBank(unittest.TestCase):
#     def test_sa(self):
#         sa = cb.SA('Aditya')
#         assert sa.b == 1000
#
#     def test_ca(self):
#         sa = cb.CA('ABC Ltd')
#         assert sa.b == 0
#
#     def test_sa_credit(self):
#         sa = cb.SA('Aditya')
#         sa.credit(100)
#         assert sa.b == 1100
#
#     def test_ca_credit(self):
#         sa = cb.CA('ABC Ltd')
#         sa.credit(100)
#         assert sa.b == 100
#
# if sys.argv[1] == 'ca':
#     ca_ts = unittest.TestSuite()
#     ca_ts.addTest(TestBank('test_ca'))
#     ca_ts.addTest(TestBank('test_ca_credit'))
#     r = unittest.TextTestRunner(verbosity=3)
#     r.run(ca_ts)
# elif sys.argv[1] == 'sa':
#     sa_ts = unittest.TestSuite()
#     sa_ts.addTest(TestBank('test_sa'))
#     sa_ts.addTest(TestBank('test_sa_credit'))
#     r = unittest.TextTestRunner(verbosity=3)
#     r.run(sa_ts)
# elif sys.argv[1] == 'all':
#     sys.argv = sys.argv[:1]
#     unittest.main(verbosity=3)
# else:
#     print "Not a valid test suite"


#Version 2
# import unittest
# import core.bank as cb
#
# class TestBank(unittest.TestCase):
#     def test_sa(self):
#         sa = cb.SA('Aditya')
#         assert sa.b == 1000
#
#     def test_ca(self):
#         sa = cb.CA('ABC Ltd')
#         assert sa.b == 0
#
#     def test_sa_credit(self):
#         sa = cb.SA('Aditya')
#         sa.credit(100)
#         assert sa.b == 1100
#
#     def test_ca_credit(self):
#         sa = cb.CA('ABC Ltd')
#         sa.credit(100)
#         assert sa.b == 100
#
# unittest.main(verbosity=3)

#Version 1
# import unittest
#
# class TestBank(unittest.TestCase):
#     def test_add(self):
#         c = 3 + 4
#         assert c == 7, 'US101: expecting 7 here'
#     def test_sub(self):
#         c = 3 - 4
#         assert c == -1, 'US101: expecting -1 here'
#
#
# unittest.main(verbosity=3)