'''class Test:
    def __init__(self, x):
        self.x = x
        self.leftnode = None
        self.parent = None

    def print(self):
        print(self.x)
        print(self.leftnode)

    def set_leftnode(self, ln):
        self.leftnode = ln
        self.leftnode.set_parent(self)
        return ln

    def set_parent(self, p):
        self.parent = p

t = Test(2)
t.print()
t2 = Test(4)
t.set_leftnode(t2).print()'''

'''d = {}
d[1] = 'red'
d[2] = 'blue'
print(d[2])
x = d[1]'''
'''                       16

            15                    17

      12          25        13          19

   11     28                         18     26

10'''
'''
import math
for i in range(int(input())):
    cnt = 0
    n = int(input())
    status = True
    while status:
        if n <= 2048:
            b = bin(n)
            for j in b:
                if j == '1':
                    cnt += 1
            print(cnt)
            status = False
        else:
            cnt += 1
            n = n - 2048'''

'''t  = int(input())
for k in range(t):
    amt = int(input())
    
    def menu_items(amt):
        
        price_list = [2**i for i in range(11, -1, -1)]
        count  = 0
        
        for price in price_list:
            while(amt>=price):
                amt = amt - price
                count +=1 
        print(count)
    menu_items(amt)'''

'''def ps(d,n):
    sum = 0
    for i in range(1, d*n+1):
        sum += i
    return sum
    
for i in range(int(input())):
    d,n = map(int, input().split())
    print(ps(d,n))'''

#Lapindrome
'''for i in range(int(input())):
    s = input()
    d = {}
    mid = int(len(s)/2)
    startstr = s[:mid]
    if len(s) % 2 != 0:
        endstr = s[mid+1:]
    else:
        endstr = s[mid:]
    
    startstr = sorted(startstr)
    endstr = sorted(endstr)
    if startstr == endstr:
        print("YES")
    else:
        print("NO")'''

#Smallest Pair
'''T = int(input())
for i in range(T):
    N = int(input())
    if T == 1000 and not(2 <= N <= 100):
        break
    if T == 10 and not(2 <= N <= 10**5):
        break
    s = input().split()
    lst = [int(i) for i in s]
    if max(lst) <= 10**6 and min(lst) >= 1:  
        lst.sort()
        print(lst[0]+lst[1])
    else:
        break'''

#Sums in a Triangle
'''T = int(input())  
for i in range(T):
    n = int(input())
    lst = []
    for j in range(n):
        cols = input().split()
        lst.append([int(i) for i in cols])
    for r in range((n-1),0,-1):
        for c in range(len(lst[r])-1):
            if lst[r][c] > lst[r][c+1]:
                lst[r-1][c] = lst[r][c] + lst[r-1][c]
            else:
                lst[r-1][c] = lst[r][c+1] + lst[r-1][c]
    print(lst[0][0])'''

#Grade the Steel
'''HARDNESS = 1
CARBON = 2
TENSILE = 4
d = {7:10,3:9,6:8,5:7,1:6,2:6,4:6,0:5}
for i in range(int(input())):
    h,c,t = map(float, input().split())
    result = 0
    if h > 50:
        result |= HARDNESS
    if c < 0.7:
        result |= CARBON
    if t > 5600:
        result |= TENSILE

    print(d[result])'''

#Cutting Recipes
'''def gcdcal(x,y):
    while y:
        x, y = y, x%y
    return x

for i in range(int(input())):
    lst = []
    
    n = input().split()
    lst.append([int(i) for i in n])
    for j in lst:
        j.pop(0)
        num1 = j[0]
        num2 = j[1]
        s = ''
        gcd = gcdcal(num1,num2)
        if len(j) > 2:
            for k in range(2,len(j)):
                gcd = gcdcal(gcd,j[k])
            for k in range(len(j)):
                s += str(int(j[k]/gcd)) + ' '
            print(s)
        else:
           print(str(int(j[0]/gcd)) + ' ' + str(int(j[1]/gcd)))'''

'''
#Ambiguous Permutation

#Inefficient Method
def permute(n): 

    if 1 <= n <= 100000:

        perm = input().split()
        if n == 1:
            print("ambiguous")
            return
        permlist = [int(k) for k in perm]
        if permlist[0] == n:
            for j in range(1, len(permlist)):
                if permlist[j] != j:
                    print("ambiguous")
                    return
            else:
                print("not ambiguous")
        
        else:
            cnt = 0
            status = True
            for j in range(permlist.index(n)):
                if permlist[j+1] - permlist[j] != 1:
                    print("ambiguous")
                    status = False
                    return
                else:
                    cnt += 1
            if status:
                if cnt != len(permlist) - 2:
                    permlist = permlist[permlist.index(n)+1:]
                    for j in range(len(permlist)-1):
                        if permlist[j+1] - permlist[j] != 1:
                            print("ambiguous")
                            return
                else:
                    print("not ambiguous")

for i in range(int(input())):                
    n = int(input())
    permute(n)
                
#Efficient Method
#2 3 4 5 1
#5 1 2 3 4

#1 4 3 2
#1 4 3 2

#7 6 5 4 3 2 1 8
#7 6 5 4 3 2 1 8
while int(input())!=0:
    a = list(map(int,input().split()))
    b = [0]*len(a)
    for i in range(len(a)):
        b[a[i]-1] = i+1
    if(a==b):
        print("ambiguous")
    else:
        print("not ambiguous")'''

'''from datetime import datetime
from dateutil.relativedelta import relativedelta
now = datetime.utcnow()
buffer_mins = now + relativedelta(minutes=30)
print(type(now))
print(type(buffer_mins))'''

#Tanu & Head-Bob
'''t = int(input())
while t >= 1:
    n = int(input())
    s = str(input().lower())
    if 'i' in s:
        print("INDIAN")
    elif 'y' in s and 'i' not in s:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
    t -= 1'''

#Rectangle
'''
t = int(input())
while 1 <= t <= 1000:
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == l[1] and l[2] == l[3]:
        print("YES")
    else:    
        print("NO") 
    t -= 1'''

#Class and Inheritance Refresher
'''
class Person(object):
    def __init__(self, name):
        self.name = name
    
    def reveal_identity(self):
        print("My name is {}".format(self.name))

class Superhero(Person):
    def __init__(self, name, hero_name):
        super(Superhero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(Superhero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))

s = Superhero("Rajiv", "RajMan")
s.reveal_identity()
'''
#Generator Statement comprehension
'''
nums = [1,2,3,4,5,6,7,8,9]
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
'''
