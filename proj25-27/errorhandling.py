def f(n):
    li = [1,2,3]
    print 1/n
    print li[n]
#f(1)
#ZeroDivisionError
#f(0)
#IndexError
#f(5)

# Generic error handling
# try:
#     f(5)
# except:
#     print "Something went wrong"

try:
    f(5)
except ZeroDivisionError as zde:
    print "Cannot divide by zero: ", zde
except IndexError as ie:
    print "Check the index: ", ie
except Exception as e:
    print "Was not expecting this"