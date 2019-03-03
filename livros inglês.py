from math import ceil

#input from user
pages = int(input("How many pages/chapters are in the book? "))
days = int(input("In how many days do you want to read it? "))
dailyPages = ceil(pages/days)

print("\nYou will read {} pages in each day!\n".format(dailyPages))

#loop to show pages by day
for day in range(1, days+1):
    if dailyPages*day >= pages:
        print("Day {}: You end the book reading until page/chapter {}".format(day, pages))
        break
    else:
        print("Day {}: read until page/chapter {}".format(day, dailyPages*day))
