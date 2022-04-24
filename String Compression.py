def strcompress(s):
    length = len(s)
    i = 0
    c = ''
    count = 0
    outputstr = ''

    if length == 0:
        return ''
    while i < length:
        c = s[i]
        count = 1
        while i+1 < length and s[i] == s[i+1]:
            count += 1
            i += 1
        if count == 1:
            outputstr += c
        else:
            outputstr += (c + str(count))
        i += 1
    return outputstr

def strcompress2(s):
    length = len(s)
    if length == 0:
        return ''
    if length == 1:
        return s
    r = ''
    cnt = 1
    i = 1
    while i < length:

        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt=1

        i += 1
        
    r = r + s[i-1] + str(cnt)
    return r

s = 'AAAABBBBxxxCCCCDDDDE'
print(strcompress(s))
print(strcompress2(s))