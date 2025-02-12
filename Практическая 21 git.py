from random import randint

def rand10():
    rand = []
    for i in range(10):
        rand.append(str(randint(0,9)))
    return "".join(rand)

class BankAccount:
    def __init__(self, owner:str, balance:float):
        self.owner = owner
        self.balance = balance
        self.account_number = rand10()
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def info(self):
        print(f"Владелец: {self.owner}\nНомер счёта: {self.account_number}\nБаланс: {self.balance}")

    def transfer(self, amount, account):
        if self.balance >= amount:
            self.balance -= amount
            account.balance += amount
        else:
            print("Недостаточно средств")

owner1 = BankAccount("Smith", 10000)
owner2 = BankAccount("Colt", 20000)
owner1.transfer(10000, owner2)
owner2.info()
