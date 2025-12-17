#slicing in list
from list1 import country
print(country[:]) #clone list
print(country[1:]); #  accessing element start with index 1
print(country[1:3]); # accssing element start with index 1 and goes to index 2 and return new list 
print(country[1::2]); # accessin element start with index and goes up to last element with skipping one value 
print(country[::-1]); # clone array in reverse order

#updating element through slicing 
country[3] = "Turkey";
print(country);
country[1:3] = ["Nepal" , "Bhutan"];
print(country); #['india', 'Nepal', 'Bhutan', 'Turkey', 'Italy', 'ukrane']
print(country[1:1]); # return Empty array
country[1:1]=["japan" , "china"]; #['india', 'japan', 'china', 'Nepal', 'Bhutan', 'Turkey', 'Italy', 'ukrane']
print(country);

country[1:3]=[];
print(country);
