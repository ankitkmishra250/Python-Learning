import math
from decimal import Decimal
import random

x= 28.4;
print(x);

# COMPLEX NUMBER
i = 2+5j;
print(i.real);
print(i.imag);


# CONVERSION
a = 10;
print(bin(a)); #0b1010
print(oct(a)); #0o12
print(hex(a)); #0xa

b = 3.4;
print(int(b)); #3
c = 32;
print(float(c)); #32.0
d = 3 ;
e = 4 ;
print(complex(d,e)); # 3+4j 


j = 16 ;
k = math.sqrt(j);
print(k); #4

print(math.ceil(4.6));  #5
print(math.floor(5.9)); #5
print(math.factorial(5)) #120
print(math.gcd(24,27)); #3


result1 = 0.3 + 0.1 + 0.2; 
print(result1); # 0.6000000000000001
result2 = Decimal("0.1") + Decimal("0.2") + Decimal("0.3");
print(result2); # 0.6

print(random.random()); # any random no appear here
print(random.randint(1,10)); # any no which is lies between 1 to 100
print(random.randint(10,100)); # any no which is lies which is between 10 to 100
print(random.choice([2,3,65,5,6,5466,5])); # any no appear here which is inside this list