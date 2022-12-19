import re

class user1:
	def __init__(self, name, gend, pasw):
		self.na = name
		self.ge = gend
		self.pa = pasw

	def verify_password(self):
		if len(self.pa)<6:
			printstr="不合法"
		m1 = re.search(r'[a-z]+', self.pa, re.I)
		m2 = re.search(r'[0-9]+', self.pa, re.I)
		if m1 and m2:
			printstr="合法"
		else:
			printstr="不合法"
		return printstr

u1 = user1("张三","男","78492")
print("u1密码:",u1.verify_password())
u2 = user1("李四","女","74638Yghd")
print("u2密码:",u2.verify_password())