def anagram(s1,s2):

    print(s1)
    print(s2)
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()
    s1list = list(s1)
    s2list = list(s2)
    print(s1list)
    print(s2list)

    while len(s1list)>0:

        k = s1list[0]
        flag = False

        for j in range(len(s2list)):
            if k == s2list[j]:
                flag = True
                s2list.pop(j)
                break
        
        if flag == True:
            s1list.pop(0)
        else:
            return False

    if s1list==[] and s2list==[]:
        return True
    else:
        return False

def anagram2(s1,s2):

    print(s1)
    print(s2)
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()
    s1list = list(s1)
    s2list = list(s2)
    s1list.sort()
    s2list.sort()
    print(s1list)
    print(s2list)
    if s1list == s2list:
        print('The given pair of lists is an Anagram!')
        return True
    else:
        print('The given pair of lists is not an Anagram!')
        return False

def anagram3(s1, s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True