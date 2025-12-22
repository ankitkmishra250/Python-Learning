# function with *args 
# write a function that takes variable number arguments and returns their sum.

def sum_all(*args):
    print(args);
    print(*args); 
    sum = 0 ;
    for e in args:
        sum=sum+e; 
    return sum;
    

print(sum_all(1,2,3,3,5,6,7));
print(sum_all(1,2,3,3,5,6,7,8));

def sum_of_all(*args):
    return sum(args);

print(sum_of_all(1,2,3,3,5,6,7,8));