countries = {
    "Egypt":"Cairo",
    "Canada":"Ottawa",
    "China":"Beijing",
    "United Arab Emirates":"Abu Dhabi"
}

print(countries)

while True:
   print("1: list all the countries and capitals")
   print("2: add another country with a captial")
   print("3: modify a contry and its capital")
   print("4: delete a countryvand its capital")
   print("5: exit the loop")
   answer = int(input())
   if answer == 1:
    print(countries)
   elif answer == 2:
    key = input("enter country name")
    value = input("enter the capital of your country")
    countries[key] = value
   elif answer == 3:
    key = input("change the name of the country")
    value = input("change the name of the capital to the new country")
    countries[key] = value
   elif answer == 4:
    key = input("choose the country you would like to delete")
    del(countries[key])
   elif answer == 5:
    break
