# Create a function that return both area and circumference of a circle given its radius.
import math

def circle(r):
    area = round((math.pi * r ** 2),2);
    circumference = round((2 * math.pi * r ),2);
    #return f" area of circle {area} \n circumference of circle {circumference}";
    return area , circumference ;

# result = circle(5);
result1 , result2 = circle(5);
print("area of circle",result1);
print("circumference of circle",result2);
