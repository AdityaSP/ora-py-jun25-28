def count_oct(ip_list):
    status = True
    if len(ip_list) != 4:
        print "Wrong octs. Mal formed IP. Exiting..."
        status = False
    return status
    
def range_check(ip_list):    
    status = True
    for oct in ip_list:
        if  not 1 <= int(oct) <= 255:
            print "Not in range. Mal formed IP. Exiting", oct
            status = False
    return status
            
def validate(ip_list):
    return count_oct(ip_list) and range_check(ip_list)

def compute_next(ip_list):
    ip_list[-1] = str(int(ip_list[-1]) + 1)
    return ".".join(ip_list)

ip = raw_input('Enter your ip adress: ')
ip_list = ip.split('.')

is_valid = validate(ip_list)
if not is_valid:
    exit()

next_ip = compute_next(ip_list)
print next_ip