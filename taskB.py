def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def chase_time_steps(A, B, V):
    total_distance = B - A
    time_to_halfway = total_distance / (2 * V)
    
    gcd_value = gcd(int(time_to_halfway), 1)
    
    steps = int(time_to_halfway) // gcd_value
    
    return steps

input_str = "1 2 1"
A, B, V = map(int, input_str.split())
result = chase_time_steps(A, B, V)
print(result)
