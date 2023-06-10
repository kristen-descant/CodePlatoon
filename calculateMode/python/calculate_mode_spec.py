# Write your own unit tests here!
from calculate_mode import calculate_mode

print(calculate_mode([1,2,3,3]))         # => [3]
print(calculate_mode([4.5, 0, 0]))       # => [0]
print(calculate_mode([1.5, -1, 1, 1.5])) # => [1.5]
print(calculate_mode([1,1,2,2]))         # => [1,2]
print(calculate_mode([1,2,3]))          # => [1,2,3], because all occur with equal frequency
print(calculate_mode(["who", "what", "where", "who"])) # => ["who"]