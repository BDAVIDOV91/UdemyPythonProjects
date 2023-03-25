class Account:
    
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
            
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount
            
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
            

class Checking(Account):
    """This class generates checking account objects"""
    
    type = 'checking'
    
    def __init__(self,filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        
        
aleks_checking = Checking('aleks_balance.txt', 1)
aleks_checking.transfer(500)
print(aleks_checking.balance)
aleks_checking.commit()
print(aleks_checking.type)

bobby_checking = Checking('bobby_balance.txt', 1)
bobby_checking.transfer(200)
print(bobby_checking.balance)
bobby_checking.commit()
print(bobby_checking.type)