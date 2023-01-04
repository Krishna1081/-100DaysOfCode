# Lists is a data structure 
# data structure: it is a way to organise and store data
# States of USA can be stored in a list 
# Order of the queue can also be done using lists

# Syntax: 
fruits = ["item1","item2"]

# Store states of India
states_of_india = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
                  "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka",
                  "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram"]
print(states_of_india[0])
# Why it starts with 0 because the thing is offset from the first element like from 0 to 1 to 2 ....

print(states_of_india[-1])

# Alteration is possible as well

states_of_india[1] = "ArunChal Pradesh"
print(states_of_india)

# Adding of elements is also possible 
states_of_india.append("Krishna Land")
print(states_of_india)

len_of_states = len(states_of_india)
print(states_of_india[len_of_states-1])

fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits,vegetables]

print(dirty_dozen)
