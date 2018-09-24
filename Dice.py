import random
while True:
	a=input("enter r to roll dice")
	r=random.randint(1,6)
	if(a=='r'):
		print(r)
	else:
		break