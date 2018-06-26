import subprocess
print subprocess.__file__

output_lines = subprocess.check_output('tasklist', shell=True).split('\n')
pids = [line.split()[1] for line in output_lines if 'firefox.exe' in line]

for pid in pids:
    subprocess.call('taskkill /f /pid ' + pid)

# top 3 processes
# total memory consumed

# Version 1
# # execute tasklist and collect the command output
# import subprocess
# output = subprocess.check_output('tasklist', shell=True)
# print output[:500]
# print "-" * 50
# # collect pids of all chrome processes
# # no need of a seperate code for split can do it along with check_output
# output_lines = output.split('\n')
# print output_lines[:5]
# print len(output_lines)
# print "-" * 50
#
# # choice is driven by the usage of lambda. filters and map with
# # lambdas are slower than comprehension
# # filter followed by a map can be replaced by a comprehension
# chrome_lines = filter(lambda line : 'chrome.exe' in line, output_lines )
# print chrome_lines[:5]
# print len(chrome_lines)
# print "-" * 50
#
# chrome_lines = [line for line in output_lines if 'chrome.exe' in line]
# print chrome_lines[:5]
# print len(chrome_lines)
# print "-" * 50
#
# pids = map(lambda line: line.split()[1], chrome_lines)
# print pids
# print len(pids)
# print "-" * 50
#
# pids = [line.split()[1] for line in chrome_lines]
# print pids
# print len(pids)
# print "-" * 50
# # execute taskkill /f /pid <pid> for each of the pids
# for pid in pids:
#     subprocess.call('taskkill /f /pid ' + pid)