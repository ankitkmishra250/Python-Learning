class Account:
    def __init__(self , name , age , contact_no , balance  ):
        self.name = name 
        self.age = age 
        self.contact_no =  contact_no
        self.balance = balance

    def checkDetail(self):
        print( f"Name : {self.name} \nAge : {self.age} \nContact_no : {self.contact_no} \n")
    
    def checkBalance(self):
        print (f"Remaining Balance : {self.balance}")
    
    def withdrawBalance(self ,wBalance):
        if wBalance <= self.balance:
            self.balance-=wBalance
            return f"withdrawl Balance = {wBalance} : Remaining balance ={self.balance}"
        else:
            return "Insufficeint Ballence"
            

class UpdatedAccount(Account):
    def __init__(self , name , age , contact_no , balance ,gender ):
        super().__init__( name , age , contact_no , balance)
        self.gender = gender 
    
    def depositAmount(self , dBalance):
        self.balance += int(dBalance)
        return f"Deposit Balance = {dBalance} : Remaining balance ={self.balance}"
    
    def checkDetail(self):
        print( f"Name : {self.name} \nAge : {self.age} \nContact_no : {self.contact_no} \nGender : {self.gender}\n")

account_01 = Account("Ankit Mishra" , 25 , "1234567891" , 25000);
# account_01.checkDetail();
# print(account_01.withdrawBalance(5000))
# print(account_01.withdrawBalance(10000))
# print(account_01.withdrawBalance(10000))
# print(account_01.withdrawBalance(20000))

account_02 = UpdatedAccount("Ankit Mishra" , 25 , "1234567891" , 35000 , "male")
print(account_02.depositAmount(5000))
# print(account_02.checkDetail())