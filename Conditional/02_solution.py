age = int(input("Tell me Your age"));
day = input("Tell me day ")

price = 12 if age >=18 else 8

if day == "wednesday":
    price -= 2;

print("Your ticket price is $",price);
