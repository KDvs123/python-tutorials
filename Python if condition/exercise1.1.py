#Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user 
# to enter a city name and it should 
# tell which country the city belongs to


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name=input("Enter a city name: ")

if(city_name in india):
    print(city_name , " is in india")
elif city_name in pakistan:
    print(city_name, " is in pakistan")
elif city_name in bangladesh:
    print(city_name, " is in bangladesh ")
else:
    print("Based on the knowledge that i have this city doesnt belongs to any of those three countries")