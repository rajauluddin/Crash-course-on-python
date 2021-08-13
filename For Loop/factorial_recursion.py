def factorial(n):
    print("Factorial called with "+ str(n))
    if n<2:
        print("returning 1")
        return 1
    result = n*factorial(n-1)
    print("returning "+ str(result)+ " for factorial of " + str(n))
    return result
factorial(5)
