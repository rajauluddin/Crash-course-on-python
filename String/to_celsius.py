#string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
# string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
# string.count(substring) Returns the number of times substring is present in the string
# string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
# string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
# string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
# string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
# delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3}F | {:>6.2f} C".format(x,to_celsius(x)))
    