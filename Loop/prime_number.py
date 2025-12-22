number = int(input("Enter a Number \n"));

is_prime = None ;

if number > 1:
    for i in range (2,number):
        if (number % i == 0):
            is_prime = False;
            break;
        else:
            is_prime = True;

print(is_prime);
