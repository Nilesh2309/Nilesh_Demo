print('Hello')
print('this is been just a sample file')
print('just pushing this file to github')
print('doing it for learning purpose ')

#hashable object
print()
print('hashable objects')
print("string_check")
print(hash("Hello"))
print("integer_check")
print(hash(42)) 
print("tuple_check")
print(hash((1,5,6)))   
print("list")
try:
    print(hash([1,80,6]))
except:
    print("list item is not hashbale")
# Checking with hasattr
print(hasattr("Hello", "__hash__"))  # True
print(hasattr([2,3,4], "__hash__"))       # False