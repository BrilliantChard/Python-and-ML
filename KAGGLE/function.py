
def least_difference(a, b, c):

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)

    return min(diff1, diff2, diff3)

print(least_difference(10, 20, 30))  # Output: 10

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)