import subprocess

# fire and forget
#subprocess.call('dir', shell=True)

# to capture the output of a command
output = subprocess.check_output('dir', shell=True)
print "the below is the output"
print "-" * 30
print output
print type(output)