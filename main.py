# Задача №1

from pyclbr import Class
from xml.dom.minidom import Node


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

# Задача №21

def string_to_array(s):
    return s.split(' ')

print(string_to_array("Robin Singh"))
print(string_to_array("CodeWars"))
print(string_to_array("I love arrays they are my favorite"))
print(string_to_array("1 2 3"))
print(string_to_array(""))

print()
# Задача №22

def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

print(zeros(6))
print(zeros(100))
print(zeros(100000))
print(zeros(30))

print()
# Задача №23

def domain_name(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    return url.split(".")[0]

print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://www.codewars.com/kata/"))
print(domain_name("https://youtube.com"))

print()
# Задача №24

def zero(op=None):
    if op is None:
        return 0
    return op(0)

def one(op=None):
    if op is None:
        return 1
    return op(1)

def two(op=None):
    if op is None:
        return 2
    return op(2)
    
def three(op=None):
    if op is None:
        return 3
    return op(3)

def four(op=None):
    if op is None:
        return 4
    return op(4)

def five(op=None):
    if op is None:
        return 5
    return op(5)

def six(op=None):
    if op is None:
        return 6
    return op(6)

def seven(op=None): 
    if op is None:
        return 7
    return op(7)

def eight(op=None):
    if op is None:
        return 8
    return op(8)

def nine(op=None):
    if op is None:
        return 9
    return op(9)


def plus(y):
    def add(x):
        return x + y
    return add

def minus(y):
    def sub(x):
        return x - y
    return sub
    
def times(y):
    def mul(x):
        return x * y
    return mul

def divided_by(y):
    def div(x):
        return x // y
    return div

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))

print()
#Задача №25

def fibonacci(n, cache={}):
    if n in [0, 1]:
        return n
    
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    
    return cache[n]

print(fibonacci(70))
print(fibonacci(50))

print()
# Задача №26

def generate_hashtag(s):
    if s == "":
        return False
    
    words = s.split()
    
    if len(words) == 0:
        return False 
    
    result = "#"
    
    for word in words:
        result += word.capitalize()
        
    if len(result) > 140: 
        return False
        
    return result 

print(generate_hashtag('CoDeWaRs is niCe'))
print(generate_hashtag('      Codewars'))
print(generate_hashtag('c i n'))
print(generate_hashtag(""))

print()
# Задача №27

# def loop_size(node):
#     slow = node
#     fast = node
    
#     while True:
#         slow = slow.next
#         fast = fast.next.next
        
#         if slow == fast:
#             break
         
#     count = 1
#     all = slow.next
    
#     while all != slow:
#         count += 1
#         all = all.next
         
#     return count

# node = Node.create_chain(1, 3)
# print(loop_size(node))

# print()
# Задача №28

def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_1 = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds_1:02}"

print(make_readable(59))
print(make_readable(60))
print(make_readable(3600))
print(make_readable(86399))

print()
# Задача №29

def alphanumeric(password: str) -> bool:
    if password == "":
        return False
    
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for simbol in password:
        if simbol not in allowed:
            return False
        
    return True
    
print("hello world_")
print("PassW0rd")
print("      ")

print()
# Задача №30
class Treenode:

    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return []
    
    result = []
    queue = [node]
    
    for all in queue:
        result.append(all.value)
        if all.left:
            queue.append(all.left)
        if all.right:
            queue.append(all.right)
            
    return result 

print(tree_by_levels((Treenode(Treenode(None, Treenode(None, None, 4), 2), Treenode(Treenode(None, None, 5), Treenode(None, None, 6), 3), 1))))
print()

# Задача №31

def balanced_parens (n):
    variants = [["", 0, 0]]
    result = []
    
    while variants:
        text, open_cnt, close_cnt = variants.pop()
        
        if len(text) == n * 2:
            result.append(text)
            
        if open_cnt < n: 
            variants.append([text + "(", open_cnt + 1, close_cnt])
            
        if close_cnt < open_cnt:
            variants.append([text + ")", open_cnt, close_cnt + 1])
            
    return result

print(balanced_parens(1))
print(balanced_parens(4))
print(balanced_parens(0))

print()
# Задача №32

def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result

print(array_diff([1,2], [1]))
print(array_diff([1,2,3], [1, 2]))
print(array_diff([], [1,2]))

print()
# Задача №33

def better_than_average(class_points, your_points):
    avn = sum(class_points) / len(class_points)
    return your_points > avn 

print(better_than_average([100, 90, 80], 70))
print(better_than_average([2, 3], 5))

print()
# Задача №34

def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"

print(abbrev_name("Sam Harris"))
print(abbrev_name("Evan C"))

print()
# Задача №35

def maps(a):
    result = []
    for x in a:
        result.append(x * 2)
    return result

print(maps([2, 5, 9]))
print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

print()