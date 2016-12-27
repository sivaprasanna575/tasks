"""bank account Class with support for deposit and withdraw operations
screenshot-anandology.com_2016-07-21_13-20-24
Convert above functionality into classes. add extra method with balance which shows actual balance"""

class Bank(object):
	def __init__(self, mainbalance=0):
		self.balance=mainbalance	
	
	def deposite(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -=amount

d = int(raw_input("Enter Deposit Amount: "))
w = int(raw_input("Enter Withdraw Amount: "))

bankaccount = Bank(0)
bankaccount.deposite(d)
bankaccount.withdraw(w)	
	
print "The Balance Amount in the Bank Account is : ", bankaccount.balance

