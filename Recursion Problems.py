def fact(n):

    if n == 0:
        return 1

    else:
        return n * fact(n-1)
        
print(fact(5))


def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

print(rec_sum(4))


def sum_func(n):
  if n < 10:
      return n  
  else:
      rem = n % 10
      calc = (n - rem) / 10
      return rem + sum_func(calc)

print(sum_func(4321))


def word_split(phrase,list_of_words, output = None):

    if phrase == '':
        return output

    status = False
    for w in list_of_words:
        if phrase.startswith(w):
            status = True
            length = len(w)
            phrase = phrase[length:]
            if output == None:
                output = []
            output.append(w)
            return word_split(phrase, list_of_words, output)

    if status == False:
        return []

print(word_split('themanran', ['the','ran','man']))
print(word_split('ilovedogsJohn', ['i','am','a','dogs','lover','love','John']))
print(word_split('themanran', ['clown','ran','man']))