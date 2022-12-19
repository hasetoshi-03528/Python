class Account:
	def __init__(self, id, name, balance):
		self.id = id
		self.na = name
		self.ba = balance

	def deposit(self, money):
		if isinstance(self.ba, (int, float)) and money >= 0:
			self.ba += money
			print(f'存入金额{money}')

	def withdraw(self, money):
		if isinstance(self.ba, (int, float)) and money >= 0:
			if self.ba - money >= 0:
				self.ba -= money
				print(f'取出金额{money}')
			else:
				print(f'可取出的金额仅为{self.ba},不可透支取出')

	def get_balance(self):
		print(f'账户余额为{self.ba}')

ID = str("005")
Name = str("张楠")
Bala = int("2000")

ac=Account(ID,Name,Bala)

ac.deposit(300)
ac.withdraw(1000)
ac.get_balance()
