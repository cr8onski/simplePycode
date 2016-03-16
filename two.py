#testing out the  mod arithmetic and discrete log, even primitive root

#start with a prime number
num = int(raw_input('enter a prime number:'))

#add a another number
root = int(raw_input('enter a smaller number:'))

#how many iterations
count = int(raw_input('how many times do you want to do this?'))

# repeatedly take number two to the current power and mod by the first number printing the count and the power and the result
print root, '^pow mod', num, count, 'many times'

for x in range(1, count+1):
    powered = pow(root, x)
    result = powered % num
    print x, powered, result, '\tdice roll ' + str(x), (result % 6 + 1)

print 'thank you have a nice day'

#prime modulus and generator

#prime factorization
msg1 = "Prime factorization of " + str(num) + ':\n'
msg2 = "You guessed right " + str(num) + ' is prime.  The prime factorization is 1, ' + str(num)
factors = []
isprime = True
for a in range(2, num/2):
    if num % a == 0:
        isprime = False
        msg1 += str(a) + ' '
        print a, num, 'Whoa Nellie!'
if isprime:
    print msg2
else:
    print msg1
