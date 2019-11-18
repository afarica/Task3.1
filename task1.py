user_text = list(input("Enter your words:").replace(' ',""))
quantity = len(user_text)
counter=1
for letter in user_text:
	if letter >= 'A' and letter <= 'Z':
		percent = round(counter*100/quantity)
		result=str(percent)+"%  capital letters "+ str(100-percent) + '%  uppercase letters'
		counter+=1
try:
	print(result)
except:
	print("All letters are uppercase")