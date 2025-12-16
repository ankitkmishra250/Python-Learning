text = "Hello Python" ;
print(text);

print(text[0]);
print(text[-1]);


# Slicing in strings 

print(text[0:4]); #Hell
print(text[1:5]); #ello
print(text[:]); #Hello Python
print(text[0::2]); #HloPto
print(text[2:]); #llo Python
print(text[::-1]); #nohtyP olleh

# String are immutable 
# Once created , Strings cannot be changed

S = "Hello";
# S[0] = "h" ❌Type Error
S = "h"+S[1:];
print(S);

# Common String Operation
a = "Hello"
b = "Python"

print(a + " " +b);  # Hello Python
print(a * 3) # Hello Hello Hello 


# String Method 
# Case Conversion
txt = "i am a Billionare Guy";
print(txt.lower());
print(txt.upper());
print(txt.capitalize());
print(txt.title());

# Checking Method 
print("abc".isalpha());
print("132".isdigit());
print("abc123".isalnum());
print(" ".isspace());

#Searching & counting 
print(txt.find("am"));
print(txt.count("a"));

# Replace & Split 
text1 = "Hello Python";
print(text1);
print(text1.replace("Python", " Java"))
print(text1.split());

#Strip(remove Space)

text = "    hello   ";
print(text.strip());
print(text.lstrip());
print(text.rstrip());