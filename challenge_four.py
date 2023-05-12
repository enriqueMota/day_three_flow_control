print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M, or L ")
add_pepperonni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if pizza_size == "S":
    bill = 15
elif pizza_size == 'M':
    bill = 20
else:
    bill = 25
    
if add_pepperonni == 'Y' and not pizza_size == 'S':
    bill += 3
    
if add_pepperonni == 'Y' and pizza_size == 'S':
    bill +=2
    
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")