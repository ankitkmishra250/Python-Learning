#f-strings
name = "Ankit";
age = 23;
print(len(name));
print(f"My Name is {name} and i am {age} years old ");

#format()

print("My Name is {} and i am {} years old ".format(name , age ));

#old method 

print("My name is %s" %name);
print("My name is %s" %age);

# Escape Character 

print("Hello\nPython");
print("Hello\tPython");
print("Hi said \"hello Python\" : ");

#memberShip Operator
myText= "Hello Java and Python";

print("Hello" in myText);
print("java" not in myText);

#looping through a string ;
for ch in name:
    print(ch);


#string comparision 
print("abc" == "abc");
print("abc" < "abb");