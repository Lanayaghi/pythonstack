class House:

	# default constructor
	def __init__(house):
		house.name = "no name"
		house.doorNum =0
		house.type = "not defined"
		house.style = "not defined"



	# a method for printing data members
	def print_house(house):
		print("house ID: ",house.name,", Doors number: ",house.doorNum,", building Type: ",house.type,", Style: ",house.style)

    
    


# creating object of the class
newHouse = House()

# calling the instance method using the object obj
newHouse.print_house()

class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor
	#setter
	def __init__(self, f, s):
		self.first = f
		self.second = s
	#getter
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()



