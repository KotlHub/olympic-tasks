def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def time_to_chase(A, B, V):
    distance = B - A
    half_of_way = distance / (2 * V)
    
    gcd_value = gcd(int(half_of_way), 1)
    
    numerator = int(half_of_way) // gcd_value
    denominator = 1 // gcd_value
    
    return f"{numerator} {denominator}"

input_str = "1 2 1"
A, B, V = map(int, input_str.split())
result = time_to_chase(A, B, V)
print(result)