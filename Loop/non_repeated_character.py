text = "teeterabcdabcd";
 
for ch in text:
    print(ch);
    if text.count(ch) == 1:
        print("Non Reapeted Char is :-",ch);
        break;