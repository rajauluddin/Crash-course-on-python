#To quickly recap the range() function when passing one, two, or three parameters:
    #One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
    #Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
    #Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x,to_celsius(x))
