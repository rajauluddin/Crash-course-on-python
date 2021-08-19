#Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. 
def convert_seconds(seconds):
    hours =seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours,minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))
print(result)
hours, minutes, seconds = result
print(hours, minutes, seconds) #we can unpack tuples
hours, minutes, seconds = convert_seconds(10000)
print(hours, minutes, seconds)
print("-------------next----")
def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21