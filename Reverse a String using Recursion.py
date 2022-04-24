def reverse(s):
    return recursive_rev(s)
    
def recursive_rev(s, ns = ''):
    if s == '':
        return ns 

    ns = s[0] + ns
    s = s[1:]
    return recursive_rev(s, ns)

print(reverse('Hello World'))


#Easy Method
def reverse2(s):

    if len(s) <= 1:
        return s

    return reverse2(s[1:]) + s[0]

print(reverse2('Hello World'))