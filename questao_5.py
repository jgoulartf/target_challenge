def inverte_string(s):
    chars = list(s)
    n = len(chars)
    for i in range(n//2):
        j = n - i - 1
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)


print(inverte_string("Python"))
print(inverte_string("Brasil"))