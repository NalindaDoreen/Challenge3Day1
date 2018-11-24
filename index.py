current_year=2018

birth=input("Enter your year of birth: ")
age=current_year-birth
if (age<18):
	print("you are a minor")
elif(age >=18 and age<=36):
	print("you are a youth")
else:
	print("you are an adult") 