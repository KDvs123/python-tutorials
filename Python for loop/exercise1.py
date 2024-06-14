#After flipping a coin 10 times you got this result,
#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]


# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

head_count=0
tail_count=0


for value in result:
    if value == "heads":
        head_count += 1
    else:
        tail_count += 1
    
print("Number of head count is: ",head_count)
print("Number of tail count is: ",tail_count)    

