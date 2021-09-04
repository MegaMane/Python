def fizzbuzz():
    for num in range (1,101):
        if num % 3 == 0 and num % 5 == 0:
            result = 'fizzbuzz'
        elif num %3 == 0:
            result = 'fizz'

        elif num % 5 == 0:
            result = 'buzz'

        else:
            result = str(num)
        
        yield result

for num in fizzbuzz():
    print(num)