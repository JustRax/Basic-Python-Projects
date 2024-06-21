import random
randomNum = random.randint(1, 100)
while True:
	guess = int(input("guess:"))
	
	if(guess ==randomNum) :
		print("You're right")
		break
	elif(guess < randomNum) :
		print("Nope too low")
	elif(guess > randomNum) :
		print("Nah too high")