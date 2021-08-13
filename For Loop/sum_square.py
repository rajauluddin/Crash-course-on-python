# For loops allow you to iterate over a sequence of values.
#Remember that a while loop is great for performing an action over and over until a condition has changed. 
#A for loop works well when you want to iterate over a sequence of elements.  
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285
print("----------next--------")
values = [23,34,56,43]
s = 0
l=0
for value in values:
    s+=value
    l+=1
print("Total sum: " + str(s) + " - Average:" + str(s/l))
