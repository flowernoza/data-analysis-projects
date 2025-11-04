# 1. Declare and assign the variables here:

shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 38400
miles_per_km = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(miles_per_km))

# Code your solution to exercises 3 and 4 here:

# 1. Create and assign a miles to Mars variable, by multiplying the distance to Mars in kilometers by the miles per kilometer.

miles_to_mars = distance_to_mars_km * miles_per_km

# 2. Creating a variable to hold the hours it would take to get to Mars, by dividing the miles to Mars by the shuttle’s speed.

hours_to_mars = miles_to_mars / shuttle_speed_mph

# 3. Declare a variable and assign it the value of days to Mars, by dividing the hours it will take to reach Mars by 24.

days_to_mars = round((hours_to_mars / 24),0)

# Print out the results of your calculations:
print(shuttle_name + " will take " + str(days_to_mars) + " days to reach Mars. ")

# Answer: Determination will take 332.67857142857144 days to reach Mars. After rounding the output, the answer will be 333 days.

# Code your solution to exercise 5 here:
#1 Creating a miles to Moon variable
miles_to_moon = distance_to_moon_km * miles_per_km
#2 Creating variable to hold hours spend to reach the Moon
hours_to_moon = miles_to_moon / shuttle_speed_mph
#3 Calculating days to Moon
days_to_moon = round((hours_to_moon / 24),2) 
print(shuttle_name + " will take " + str(days_to_moon) + " days to reach the Moon. ")

# Answer: Determination will take 0.06 days to reach the Moon.