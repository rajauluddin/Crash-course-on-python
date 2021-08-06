# Anatomy of a While Loop
# A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.  
x=0
while x<5:
    print("Not there yet, x=" + str(x))
    x+=1
print("Finally x="+str(x))
print("------while loop example-----------------------")
print(" ")
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(6)
print("------while loop example-----------------------")
print(" ")
def count_down(start_number):
  current = start_number
  while current > 0:
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
print("------while loop example-----------------------")
print(" ")
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= 5:
		print(n)

print_range(1, 5)