country = input('Which country are you from?:')
age = input('How old are you?:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You are qualified to have a driving test!')
	else:
		print("You arn't qualified to have a driving test!")
elif country == 'USA':
	if age >= 16:
		print('You are qualified to have a driving test!')
	else:
		print("You arn't qualified to have a driving test!")
else:
	print('You can only enter Taiwan or USA!')