import math

	
def main(side1, side2, side3):
    if valid_sides(side1,side2,side3) == True:
        print ("Area of the triangle is:", compute_area(side1,side2,side3))
    else:
        print ("Sides", "("+str(side1)+",", str(side2)+",", str(side3)+")", "cannot build a triangle.")

def valid_sides(side1, side2, side3):
	"""Function valid_sides returns True if input sides can build a triangle.
           Input: side1, side2, side3; type: float
	   Output: True or False; type: boolean	
	"""
	if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2 and side1 > 0 and side2 > 0 and side3 > 0:
		return True
	else:
		return False

def compute_area(side1,side2,side3):
	"""Function compute_area computes the area of the triangle.
           Input: side1, side2, side3; type: float
           Output: area; type: float	
	"""
	s = (side1+side2+side3)/2
	area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
	return area

side1 = float(input("Enter first side of triangle: "))
side2 = float(input("Enter second side of triangle: "))
side3 = float(input("Enter third side of triangle: "))

# main method
main(side1,side2,side3)


