# Задача №1

def past(h, m, s):
    result = (h * 3600 + m * 60 + s) * 1000
    return result
print(past(0, 1, 1))

print()
# Задача №2

def find_uniq(xs):
    for i in xs:
        if xs.count(i) == 1:
            return i
print(find_uniq([1, 1, 2, 1, 1]))

print()
# Задача №3

def has_subpattern(strng):
    for i in range(1, len(strng)):
        if len(strng) % i == 0:
            part = strng[:i]
            if part * (len(strng) // i) == strng:
                return True
    return False

print(has_subpattern("acacac"))
print(has_subpattern("aklfgb"))
print(has_subpattern("ababab"))

print()
# Задача №4

def is_square(n):    
    if n < 0: 
        return False
    for i in range(n + 1):
        if i * i == n:
            return True
        
    return False

print(is_square(-1))
print(is_square( 0))
print(is_square( 3))
print(is_square( 4))
print(is_square(25))
print(is_square(26))

print()
# Задача №5

def make_upper_case(s):
    return s.upper()
print(make_upper_case("hello"))

# Задача №6
def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False

print(hero(18, 5))
print(hero(23, 17))

print()
# Задача №7

def greet():
    return "hello world!"
print(greet())

print()
# Задача №8

def get_age(age):
    return int(age[0])
print(get_age("2 years old"))
print(get_age("4 years old"))
print(get_age("5 years old"))
print(get_age("7 years old"))

print()
# Задача №9

def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([34, 15, 88, 2,]))
print(find_smallest_int([34, -345, -1, 100]))

print()
# Задача №10

def invert(list):
    return [-x for x in list]
print(invert([-1, -2, -3, -4, -5]))
print(invert([-1, 2, -3, 4, -5]))
print(invert([]))

print()