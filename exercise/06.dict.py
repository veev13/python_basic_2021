message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

dictionary = {}
for c in message:
    if dictionary.get(c) is None:
        dictionary[c] = 1
    else:
        dictionary[c] += 1
print(dictionary)
