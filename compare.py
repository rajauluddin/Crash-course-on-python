# print(1 != 2)
# print(25 > 50 or 25< 52)
# print(not 42 == "Answer" )
def num(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)
print(num(10))
print("big" > "small")
print(11 % 5)