def sentrev1(s):
    w = s.strip().split()
    print('W:',w)
    rev = ''
    for word in range((len(w)-1),-1,-1):
        rev += w[word] + ' '
    rev = rev.rstrip()
    print('1. Reversed Sentence:',rev)
    return rev

def sentrev2(s):
    w = s.strip().split()
    print('W:',w)
    rev = ' '.join(reversed(w))
    print('2. Reversed Sentence:',rev)
    return rev

def sentrev3(s):
    w = s.strip().split()
    print('W:',w)
    rev = ' '.join(w[::-1])
    print('3. Reversed Sentence:',rev)
    return rev

def sentrev4(s):
    word = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        if s[i] not in spaces:

            wordstart = i

            while i < length and s[i] not in spaces:
                i += 1
            word.append(s[wordstart:i])

        i += 1
    rev = ''
    for i in range((len(word)-1),-1,-1):
        rev += word[i] + ' '
    rev = rev.rstrip()
    print('4. Reversed Sentence:',rev)
    return rev

s = ' Banana is a fruit '
sentrev1(s)
sentrev2(s)
sentrev3(s)
sentrev4(s)