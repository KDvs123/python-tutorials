d={"Tom":734342343,"rob":21325245,"joe":3424234324}
d
{'Tom': 734342343, 'rob': 21325245, 'joe': 3424234324}
d["Tom"]
734342343

# Changin the value in a dictionary

d["sam"]=21321432523
d
{'Tom': 734342343, 'rob': 21325245, 'joe': 3424234324, 'sam': 21321432523}
d["rob"]=132123123
d
{'Tom': 734342343, 'rob': 132123123, 'joe': 3424234324, 'sam': 21321432523}
del d["sam"]
d
{'Tom': 734342343, 'rob': 132123123, 'joe': 3424234324}

# displaying the dictionary values

# 1. One way

for key in d:
    print("Key is: ",key," value is ",d[key])

# 2. Two way

for key , value in d.items():
    print("Key is ",key, " Value is ",value)

    
# Search for a value in dictionary

"tom" in d
False
"Tom" in d
True

# Wipe out the data in a dictionary

d.clear()
