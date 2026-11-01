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