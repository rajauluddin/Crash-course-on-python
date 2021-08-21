def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter]+=1
    return result
print(count_letters("abcdeefgh"))
print(count_letters("a quick brown fox jumps over a lazy dog"))
print(count_letters("this is a short text"))
print(count_letters("this is for the course sake i want to learn python"))

