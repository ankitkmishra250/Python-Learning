my_list = ["banana","mango","guava","banana","cherry","mango","pineapple"];
#my_list = ["banana","mango","guava","cherry","pineapple"];

unique_item = set();

for item in my_list:
    if item in unique_item:
        print("Duplicates item  are present in list :-",item);
        exit();
    unique_item.add(item);
print("list are unique");

       