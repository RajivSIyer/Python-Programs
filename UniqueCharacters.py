def UniqChar1(s):
    return len(s) == len(set(s))

def UniqChar2(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

s = 'ABCDE'
print(UniqChar1(s))
s = 'AABCDE'
print(UniqChar1(s))

s = 'ABCDE'
print(UniqChar2(s))
s = 'ABCDEA'
print(UniqChar2(s))