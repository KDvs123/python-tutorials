# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width

def calculate_area(base,height,shape="trangle"):
    area=0
    if(shape=="trangle"):
        area= (1/2) * base *height
    elif(shape=="rectangle"):
        area=base*height
    
    return area

area_of_a_trangle=calculate_area(5,6,"trangle")
area_of_a_rectangle=calculate_area(5,6,"rectangle")

print("Area of a trangle is: ",area_of_a_trangle)
print("Area of a rectangle is: ",area_of_a_rectangle)


    

    