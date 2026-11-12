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
# Задача №11

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name  + " plays banjo"
    else:
        return name + " does not play banjo"
    
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("bravo"))
print(are_you_playing_banjo("rolf"))

print()
# Задача №12

def high_and_low(numbers):
    nums =[int(x) for x in numbers.split()]
    biggest = max(nums)
    smallest = min(nums)
    return f"{biggest} {smallest}"
print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5"))
print(high_and_low("1 9 3 4 -5"))

print()
# Задача №13

def litres(time):
    return int(time // 2)
print(litres(3))
print(litres(6.7))
print(litres(11.8))

print()
# Задача №14

def solution(string):
    return string[::-1]
print(solution('world'))
print(solution('word'))

print()
# Задача №15

def bool_to_word(boolean):
    if boolean == True:
        return "Yes" 
    else:
        return "No"
        
print(bool_to_word(True))
print(bool_to_word(False))
print(bool_to_word(False))

print()
# Задача №16

def get_count(sentence):
    count = 0
    for char in sentence:
        if char in "aeiou":
            count +=1
    return count

print(get_count("abracadabra"))
print(get_count("pear tree"))

print()
# Задача №17

def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4,6)

print(validate_pin("1234"))
print(validate_pin("1.234"))
print(validate_pin("ad234"))

print()
# Задача №18

def check(seq, elem):
    return elem in seq
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))
print(check(["what", "a", "great", "kata"], "kat"))
print(check([78, 117, 110, 99, 104, 117, 107, 115], 99))

print()
# Задача №19

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l + w) * 2
    
print(area_or_perimeter(4, 4))
print(area_or_perimeter(6, 10))

print()
# Задача №20

def remove_char(s):
    return s[1:-1]

print(remove_char("eloquent"))  
print(remove_char("country"))  
print(remove_char("person"))    
print(remove_char("place"))
print(remove_char("ok"))
print(remove_char("ooopsss"))

print()
