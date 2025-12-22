# default parameter value 

def greets(name = "User"):
    return f"Hello ! {name}"

person1 = greets("Ankit");
person2 = greets();

print(person1);
print(person2);
