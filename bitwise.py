# odd and even check using bit wise

for i in range(1, 10):
    # check for odd
    
    if i & 1:
        print(f"Odd Number = {i}")
    if ~i & 1:
        print(f"Even Number = {i}")
        
# multiplication and division using bitwise
# x >> 1 (means dividing by 2)
# x << 1 (means multipying by 2)
a = pow(2, 10)

for i in range(1, 10):
    divide = a >> i
    multiply = a << i
    
    print(f"{i} divide = {divide}, multiply = {multiply}")