# accept an input
ui = raw_input('Enter a string: ').lower()

# check the reverse against the original
# Madam == madaM

if ui[::-1] == ui:
    print "Its a palindrome!"
else:
    print "Its not a palindrome!"
    