import time
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0
def triangle(x1, y1, x2, y2, x3, y3):
    try:
        pointArray = Input.split(",")
        x1 = float(pointArray[0])
        y1 = float(pointArray[1])
        x2 = float(pointArray[2])
        y2 = float(pointArray[3])
        x3 = float(pointArray[4])
        y3 = float(pointArray[5])
        p = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2.0
        return p
    except:
        print("Uh Oh. Do it again.")
        p = 0
        return p

        
while True:
    Input = input("Points: ")

    area = triangle(x1, y1, x2, y2, x3, y3)
    if area == 0:
        print("Are you sure thats a triangle?")
        continue
    else:
        print("Here is yo area! " + str(area))