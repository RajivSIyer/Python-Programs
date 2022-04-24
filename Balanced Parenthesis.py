'''def balance_check(s):

    d = {'(':1, '[':1, '{':1, ')':-1, ']':-1, '}':-1}
    x = 0

    for c in s:
        x += d[c]

    if x != 0:
        return False
    else:
        return True

print(balance_check('[](){[()]}'))
print(balance_check('[(]{}'))'''

def balance_check(s):

    opening = set('([{')
    matches = set([('(',')'), ('[',']'), ('{','}')])
    stack = []

    if len(s)%2 != 0:
        return False

    for paran in s:

        if paran in opening:
            stack.append(paran)
        
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paran) not in matches:
                return False
    
    return len(stack) == 0 

print(balance_check('[](){[()]}'))
print(balance_check('[(]{}'))