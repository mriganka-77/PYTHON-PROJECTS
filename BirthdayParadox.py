import random

birthday = []
i = 0

while i < 50:
    year = random.randint(1900, 2023)

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = 1
    else:
        leap = 0

    month = random.randint(1, 12)

    # Determine the maximum day of the month
    if month == 2:
        day = random.randint(1, 29 if leap else 28)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    birthday.append(f"{day:02d}-{month:02d}-{year}")
    i += 1

# Print the birthdays
for b in birthday:
    print(b)
