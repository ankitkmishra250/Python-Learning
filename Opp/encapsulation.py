class Account:
    def __init__(self, name , age , gender , contact_no , balance ):
        self.name = name 
        self.age = age 
        self.gender = gender 
        self.__contact_no = contact_no
        self.__balance = balance
    
    def get_contanct_no(self):
        return f"+91{self.__contact_no}"
    
    def get_balance(self):
        return f"{self.__balance}.00"
    
class Account_01(Account):
    def __init__(self , name , age , gender , contact_no , balance , account_no):
        super().__init__(name , age , gender , contact_no , balance)
        self.__account_no = account_no 
        self.__balance = balance 
    
    def get_balance(self):
        return f"{self.__balance}.00"

    def get_account_no(self):
        return f"{self.__account_no}"
    
    def withdraw_amount(self , amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"{amount} is Successfully Withdrawl \n Remaining Balance is {self.__balance}.00"
        else:
            return f"Transaction Failed ! Insufficient Amount\n Remaining Balance is {self.__balance}.00"
    
    def deposit_amount(self , amount):
        self.__balance += amount
        return f"{amount} is Successfully Credited in your bank account \n Remaining Balance is {self.__balance}.00"


person1 = Account("Ankit Mishra" , 23 , "male" , "1234567890" , 2500000)
print(person1.get_balance())

person2 = Account_01("Ankita Mishra" , 23 , "female" , "1234667890" , 250000 , 125412541254)
# print(person2.name)
# print(person2.age)
# print(person2.gender)
# print(person2.get_account_no())

print(person2.get_account_no())
print(person2.withdraw_amount(50000))
print(person2.deposit_amount(61000))

