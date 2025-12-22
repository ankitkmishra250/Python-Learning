text = "NoteBook";
rev = ""

for ch in text :
    rev = ch + rev ;

print(rev); 


for i in range(len(text)-1,-1,-1):
    #len(text)-1 --> loop starting (last index)
    #-1 ---> move backward (first index)
    #-1 ---> moves backward
    print(text[i] , end="");
    
