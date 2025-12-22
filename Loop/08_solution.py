
# keep asking the user input until they enter a number between 1 to  10 ;

while True: 
    number = int(input("Enter a Number between 1 to 10 \n"));
    if 1 <= number <= 10: 
    #if (number >=1 and number <=10):
        print("Thanks");
        break;
    else:
        print("invalid Input ! Try Again");