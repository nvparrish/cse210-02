import random

first_number = random.randint(1,13)
second_number = random.randint(1,13)
score = 300

print(f"The card is: {first_number}")
high_low = input("Higher or lower? [h/l]")
print(f"Next card was: {second_number}")

if second_number > first_number:
    print("h")
elif second_number < first_number:
    print("l")