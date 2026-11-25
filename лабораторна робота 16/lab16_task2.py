import pylab  
import numpy as np  

n = int(input('Введіть тризначне число: '))
while n < 100 or n > 999:
    print('Число має бути тризначним')
    n = int(input('Введіть тризначне число: '))

a = n  
factors = [] 
d = 2 
while d * d <= a:  
    while a % d == 0: 
        factors.append(d)  
        a = a // d 
    d += 1
if a > 1: 
    factors.append(a)

print(n, '=', ' * '.join(map(str, factors))) 

primes = sorted(set(factors)) 
counts = [factors.count(p) for p in primes] 
for p, c in zip(primes, counts):
    print('Множник', p, 'зустрічається', c, 'раз')

x = np.arange(len(primes)) 
y = np.array(counts) 

pylab.bar(x, y) 
pylab.xticks(x, [str(p) for p in primes])  
pylab.yticks(range(0, max(counts) + 1))  
pylab.xlabel('Простий множник')
pylab.ylabel('Частота')
pylab.title('Гістограма частот множників числа ' + str(n))
pylab.savefig('hist.png', dpi=300) 
pylab.show()  