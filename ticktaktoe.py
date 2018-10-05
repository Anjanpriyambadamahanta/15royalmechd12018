a=['1','2','3','4','5','6','7','8','9']

def print_Board():
	print(a[0],'|',a[1],'|',a[2])
	print("----------")
	print(a[3],'|',a[4],'|',a[5])
	print("----------")		
	print(a[6],'|',a[7],'|',a[8])

playerOneTurn = True
while True:
	print_Board()
	p=input("choose a a place:")
	If(p in a):
	if(a[int(p)-1]=='x' or a[int(p)-1]=='o'
		print("place taken,choose another place...")
		continue
	else:
		a[int(p)-1]='x'
else:
	if playerOneTurn:
		a[int(p)-1]='x'
		playerOneTurn=not playerOneTurn
	else:
		a[int(p)-1]='o'
		playerOneTurn=not playerOneTurn


