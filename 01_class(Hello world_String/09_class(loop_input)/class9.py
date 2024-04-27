import sys

print("Line1")
print("Line2")

print(type(sys.argv))

if sys.argv[1] == '-g':
    print("Package to be installed globally")

print(sys.argv) # iterative data type list[str] 0 = filename USER DEFINED
