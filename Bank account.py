class Bank_acc(object):
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.pin = 1234
        self.interest = 0.006
        self.acc_num = 123456789

    def credit_acc(self):
        amount = float(input("Enter your deposit"))
        self.balance += amount

    def debit_acc(self):
        get_pin = int(input("Enter your pin number"))
        if get_pin != self.pin:
            print("That's not correct.")
        else:
            amount = float(input("Enter your withdraw amount"))
            self.balance -= amount

par_acc = Bank_acc()
par_acc.name = "Parker"
print(par_acc)
par_acc.credit_acc()
print(par_acc.balance)
par_acc.debit_acc()
print(par_acc.balance)