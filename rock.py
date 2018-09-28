import random

a={1:'r',2:'p',3:'s'}

while True:
	p=input("your choice r/p/s:")
	c=a[random.randint(1,3)]

	print("your choise:",p,"computer choise:",c)
	
	if(p==c):
		print('  **Draw!** ')
	elif(p=='rock' and c=='paper'):
		print('\t\t ## you lose! ##\t\t')
	elif(p=='rock' and c=='scissor'):
		print('\t\t ## you win! ##\t\t')
	elif(p=='paper' and c=='rock'):
		print('\t\t ## you win! ##\t\t')
	elif(p=='paper' and c=='scissor'):
		print('\t\t ## you lose! ##\t\t')
	elif(p=='scissor' and c=='rock'):
		print('\t\t ## you lose! ##\t\t')
	elif(p=='scissor' and c=='paper'):
		print('\t\t ## you win! ##\t\t')







