import sys, random

valid_years = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]

def sum_int(inp):
    return sum(int(x) for x in str(inp))

def generate_oem():
    rand_day = f'{random.randrange(367):03}'
    rand_year = random.choice(valid_years)

    key_first = rand_day + rand_year
    key_second: str
    key_third = f'{random.randrange(100000):05}'

    while True:
        key_second = f'{random.randrange(1000000):07}'
        if check_oem_second(key_second):
            break

    return f'{key_first}-OEM-{key_second}-{key_third}'

def generate_retail():
    key_first: str
    key_second: str

    while True:
        key_first = f'{random.randrange(1000):03}'
        if check_retail_first(key_first) == True:
            break

    while True:
        key_second = f'{random.randrange(1000000):07}'
        if check_oem_second(key_second) == True:
            break

    return f'{key_first}-{key_second}'

def generate_office():
    key_first: str
    key_second: str

    while True:
        key_first = f'{random.randrange(10000):04}'
        if check_office_first(key_first) == True:
            break

    while True:
        key_second = f'{random.randrange(1000000):07}'
        if check_oem_second(key_second) == True:
            break

    return f'{key_first}-{key_second}'
    
def validate_oem(key):
    key_segs = key.split('-')
    return len(key_segs) == 4 and check_oem_first(key_segs[0]) and check_oem_second(key_segs[2]) and check_oem_third(key_segs[3])
    
def validate_retail(key):
    key_segs = key.split('-')
    return len(key_segs) == 2 and check_retail_first(key_segs[0]) and check_oem_second(key_segs[1])

def validate_office(key):
    key_segs = key.split('-')
    return len(key_segs) == 2 and check_office_first(key_segs[0]) and check_oem_second(key_segs[1])

def check_oem_first(key):
    if not key.isdigit():
        return False

    if len(key) != 5:
        return False
    
    key_day = key[:3]
    key_year = key[-3:]

    if key_day < 0 or key_day > 366:
        return False
    
    if key_year in valid_years:
        return False

    return True

def check_oem_second(key):
    if not key.isdigit():
        return False

    if len(key) != 7:
        return False
    
    key_int = int(key)
    key_last = key_int % 10

    if key_last == 0 or key_last > 7:
        return False

    if sum_int(key_int) % 7 != 0:
        return False
    
    return True

def check_oem_third(key):
    if not key.isdigit():
        return False
    
    if len(key) != 5:
        return False
    
    return True

def check_retail_first(key):
    if not key.isdigit():
        return False
    
    if len(key) != 3:
        return False

    rejected_first = ["333", "444", "555", "666", "777", "888", "999"]

    if key in rejected_first:
        return False
    
    return True

def check_office_first(key):
    if not key.isdigit():
        return False
    
    if len(key) != 4:
        return False
    
    key_int = int(key)

    if key_int < 1 or key_int > 9991:
        return False
    
    digit_third = int(key[2])
    digit_fourth = int(key[3])

    pos_digit_0 = digit_third + 1
    pos_digit_1 = digit_third + 2
    
    if pos_digit_0 > 9:
        pos_digit_0 -= 10
    if pos_digit_1 > 9:
        pos_digit_1 -= 10

    if digit_fourth == pos_digit_0:
        return True
    elif digit_fourth == pos_digit_1:
        return True
    else:
        return False

valid_key: bool
key_type: str

try:
    arg = sys.argv[1]
except IndexError:
    arg = False

if not arg:
    print(f'OEM key: {generate_oem()}')
    print(f'Retail key: {generate_retail()}')
    print(f'Office 97 key: {generate_office()}')
    exit()

key_segs = arg.split('-')

if 'OEM' in arg:
    valid_key = validate_oem(arg)
    key_type = 'OEM'
elif len(key_segs[0]) == 4:
    valid_key = validate_office(arg)
    key_type = 'Office 97'
else:
    valid_key = validate_retail(arg)
    key_type = 'retail'

if valid_key:
    print(f'Valid {key_type} key')
else:
    print('Invalid key')