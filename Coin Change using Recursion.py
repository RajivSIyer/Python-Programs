from nose.tools import assert_equal
import math

def rec_coin2(n, denom, l):
    
    if l == []:
        denom.sort(reverse=True)

    if len(denom) == 0:
        if n != 0:
            print("Not possible to change with provided denominations!")
        return 0

    m = n % denom[0]

    if m == 0:
        numcoins = int(n/denom[0])
        l.append((denom[0], numcoins))
        denom.pop(0)
        return numcoins

    if denom[0] > n:
        denom.pop(0)
        return rec_coin2(n, denom, l)

    numcoins = int(math.floor(n/denom[0]))
    l.append((denom[0], numcoins))
    denom.pop(0)
    return numcoins + rec_coin2(m, denom, l)

lx = []
print(rec_coin2(74,[3,7,10,25],lx))
print(lx)

def rec_coin(n, denom):
    
    
    denom.sort(reverse=True)

    if len(denom) == 0:
        return 0
    
    m = n % denom[0]

    if m == 0:
        numcoins = int(n/denom[0])
        denom.pop(0)
        return numcoins

    if denom[0] > n:
        denom.pop(0)
        return rec_coin(n, denom)

    numcoins = int(math.floor(n/denom[0]))
    denom.pop(0)
    return numcoins + rec_coin(m, denom)

print(rec_coin(45,[1,5,10,25]))
print(rec_coin(23,[1,5,10,25]))
print(rec_coin(74,[1,5,10,25]))

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        coins = [1,5,10,25]
        assert_equal(solution(23,coins),5)
        coins = [1,5,10,25]
        assert_equal(solution(74,coins),8)
        print ('Passed all tests.')
# Run Test

test = TestCoins()
test.check(rec_coin)