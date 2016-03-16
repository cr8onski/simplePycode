# Still playing with python and primes
# How many primes in your lifetime?

from datetime import datetime

print "How many primes in your lifetime?\n"
lownum = int(raw_input('Enter birth year: '))

print lownum
highnum = datetime.now().year
print highnum
msg1 = "the prime years in your lifetime are "
for yr in range(lownum, highnum + 1):
    print yr
    isprime = True
    for num in range(2, yr / 2):
        if yr % num == 0:
            isprime = False
            break
    print isprime
    if isprime:
        msg1 += str(yr) + ", "
print msg1 + " ... We wish you well."
