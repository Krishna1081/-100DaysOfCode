age = input("What is your current age? ")
current_age = int(age)
life_left = 90
years_left = (life_left * 12) - (current_age * 12 )
days_left = (life_left * 365) - (current_age *365)
weeks_left =(life_left * 52)- (current_age *52)
print(f"You have {days_left} days, {weeks_left} weeks, and {years_left} months left.")