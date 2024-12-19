nambers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes=[]
not_primes=[]
for i in range (len(nambers)):
    if nambers[i] > 1:
        is_prime = True
        for n in range(2,int(nambers[i]**0.5) +1):
            if nambers[i] % n == 0:
                is_prime = False
                not_primes.append(nambers[i])
                break
        if is_prime:
            primes.append(nambers[i])

print('Primes: ', (primes))
print('Not Primes: ', (not_primes))












