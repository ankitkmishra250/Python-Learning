#without using yield
def odd_generator(limit):
    for i in range(1,limit+1,2):
        print(i);

odd_generator(10);
print("--------------------------")
#with using yield
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i ;

for val in even_generator(12):
    print(val);

