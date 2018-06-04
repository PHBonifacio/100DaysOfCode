import sys

myint = 7
myfloat = 8.0 # mesmo que utilizar myfloat = float(8)
mystring = 'esta é uma string' # mesmo que utilizar ""
hello = "hello"
world = "world"
helloworld = hello + " " + world # soma de strings
# declaracao de listas
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(sys.version)
print(myfloat)
print(mystring)
print(helloworld)
# duas formas de escrever os dados de uma string
#print(mylist[0]) # prints 1
#print(mylist[1]) # prints 2
#print(mylist[2]) # prints 3
for x in mylist:
    print(x)
number = 1 + 2 * 3 / 4.0
print(number)