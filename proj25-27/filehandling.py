import os

# if os.path.exists('jun26.txt'):
#     print "File already exists"
#     exit()
# if os.path.isfile('jun26.txt'):
#     print "Its a file"
# print os.path.isdir('jun26.txt')

#path = r'C:\Users\Dell lap\Desktop\Python\oracle\online\jun-25-27\new26.txt'
#path = 'C:\\Users\\Dell lap\\Desktop\\Python\\oracle\\online\\jun-25-27\\new26.txt'
#path = 'C:/Users/Dell lap/Desktop/Python/oracle/online/jun-25-27/new26.txt'
# fh = open(path, 'wt')
# fh.write('Line 1')
# fh.write('\n')
# fh.write('Line 2')
# fh.close()

# fh = open(path, 'at')
# fh.write('\n')
# fh.write('I tried to append this to existing data')
# fh.close()

#fh = open('jun26.txt', 'rt')
# s = fh.read()
# print "*" * 50
# print s
# print type(s)
# print "*" * 50
# s = fh.read()
# print s
# print "*" * 50
# fh.seek(0)
# s = fh.read()
# print s
# print "*" * 50
# fh.seek(0)
# l = fh.readlines()
# print l
# print type(l)
# print "*" * 50

# fh = open('jun26.txt', 'rt')
# for line in fh:
#     print line
# fh.close()

# working with a 'context manager'
# with open('jun26.txt') as fh:
#     for line in fh:
#         print line
#
# print 'bye'