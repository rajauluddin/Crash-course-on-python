def check_no(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
print(check_no(10)) #Should be Positive
print(check_no(0)) #Should be Zero
print(check_no(-5)) #Should be Negative

print((2**2) == 4)