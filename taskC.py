import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def intersection_points(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    
    if r1 + r2 < d or d < abs(r1 - r2):
        return 0 
    
    if d == 0 and r1 == r2:
        return -1
    
    if d + min(r1, r2) == max(r1, r2) or d == r1 + r2:
        return 1
    
    return 2

input_str = "0 0 3 10 0 7"
X1, Y1, R1, X2, Y2, R2 = map(int, input_str.split())
result = intersection_points(X1, Y1, R1, X2, Y2, R2)
print(result)