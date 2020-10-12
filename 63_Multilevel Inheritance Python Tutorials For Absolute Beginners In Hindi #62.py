
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

# print(darry.guitar)

# electronic device
# pocket gadget
# phone

"""
class Ded:
	basketball = 6
class Son(Ded):
	basketball=78
	dance = 1
	def  isdance(self):
		return f"yas i dance {self.dance} no of times"
class  Grandson(Son):
	dance = 6
	def  isdance(self):
		return f" very yas i dance {self.dance} no of times"
darry = Ded()
larry= Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)

"""

