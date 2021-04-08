import sys
print(sys.version)

a = "Hello world"
c = a
print(a is c)
print(id(a))
print(id(c))
print(sys.getrefcount(a))
print(sys.getrefcount(c))
del a
print(sys.getrefcount(a))
print(sys.getrefcount(c))
