print("Enter the three interchanged values:")
a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")


print("\nEnter the correct order of the values (1 for a, 2 for b, 3 for c):")
pos1 = int(input("Position 1 should be: "))
pos2 = int(input("Position 2 should be: "))
pos3 = int(input("Position 3 should be: "))

values = [a, b, c]
correct_order = [values[pos1 - 1], values[pos2 - 1], values[pos3 - 1]]


print("\nValues in correct positions:")
print("First:", correct_order[0])
print("Second:", correct_order[1])
print("Third:", correct_order[2])