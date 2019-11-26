# Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
# регистре (заглавные) и в нижнем регистре (прописные).
user_text = list(input("Enter your words:").replace(' ',""))
quantity = len(user_text)
counter=1
counter1=1
for letter in user_text:
	if letter >= 'A' and letter <= 'Z':
		percent = round(counter*100/quantity)
		result=str(percent)+"%  capital letters "
		counter+=1
	elif letter >='a' and letter <='z':
		percent1 = round(counter1*100/quantity)
		result1=str(percent1)+"%  uppercase letters"
		counter1+=1

try:
	print(result,result1)
except:
	print("Sorry,enter only letters")
