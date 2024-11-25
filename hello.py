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

#Chainmap
print()
print("chainmaps")
from collections import ChainMap
d1=dict(a=1 , b=2)
d2=dict(a=3, b=4 , c=6)
chain=ChainMap(d1, d2)
print(chain)
print(chain['c'])

#Counter
print('counter')
import collections
ct = collections.Counter('abracadabra')
print(ct)
print("most common" , ct.most_common(4))