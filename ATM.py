class ATM:

    def transaction(self, trans, balance):
        if trans % 5 == 0:
            if (balance - trans - 0.50) < 0.00:
                return balance

            return (balance - trans - 0.50)
        else:
            return balance

amount = ATM()
trans, balance = map(float, input().split())
result = amount.transaction(trans, balance)
print("{0:.2f}".format(result))