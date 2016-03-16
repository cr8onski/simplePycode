#still wrapping my head around public private encyption
#Diffie Hellmann

primeModulus = 3
generator = 17

a = int(raw_input('enter Alice number'))

ares = pow(primeModulus, a) % generator
print 'this is what Alice sends to Bob:', a, ares, '\n'

bres = pow(primeModulus, ares) % generator
print 'this is what Bob sends to Alice:', ares, bres, '\n'

print 'now we do magic and we have the same number'
res1 = pow(primeModulus, ares*bres) % 17
res2 = pow(primeModulus, bres*ares) % 17
print res1, res2
