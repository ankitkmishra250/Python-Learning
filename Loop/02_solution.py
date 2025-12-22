
my_list = [1,-1,2,3,-4,4,-6,8,-5,7,14,-12,45,-36];
positive_no_count = 0;
for number in my_list:
    if(number >= 0):
        print(number);
        positive_no_count += 1;

print("All positive No :-",positive_no_count);