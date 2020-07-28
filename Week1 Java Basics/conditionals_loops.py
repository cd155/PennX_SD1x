# Find a prime number
# primes are integers greater than one
# prime number is divisible by 1 and the number itself

def find_prime_number(test_num):
    potential_factor = 2
    while test_num % potential_factor != 0:
        potential_factor += 1
    
    if test_num == potential_factor:
        return True
    else:
        return False

# find the output without excuting code
def quiz_one():
    n = 93
    b = 1.27
    result = n - b
    if result > 0:
        b = result < 0
        if b:
            print("answer_one")
        else:
            s = "answer_two"
            if result >= 0:
                s = "answer_two changed!"
                print(s)
            else:
                print(s)

def quiz_two():
    i = 0
    while i < 10:
        print("answer_two")

def quiz_three():
    j = 0
    for i in range(0, 93):
        j = i + 1
    i = j
    print(i)

def quiz_four():
    for i in range(0, -1):
        print("answer_four")

#test
testarrays = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("Prime numbers:")
for num in testarrays:
    if find_prime_number(num):
        print(num)

print("Quiz one:")
# quiz_one()

print("Quiz two:")
# quiz_two()

print("Quiz three:")
# quiz_three()

print("Quiz four:")
# quiz_four()