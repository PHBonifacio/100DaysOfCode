i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
second_integer = 0
second_double = 0
second_string = ""
# Read and save an integer, double, and String to your variables.
# To pass on HackerRank online tests the inputs can't print anything
#read_value = input("Type an integer\r\n")
#second_integer = int(read_value)
#read_value = input("Type an double\r\n")
#second_double = float(read_value)
#second_string = input("Type an string\r\n")
read_value = input()
second_integer = int(read_value)
read_value = input()
second_double = float(read_value)
second_string = input()
# Print the sum of both integer variables on a new line.
print(i + second_integer)
# Print the sum of the double variables on a new line.
print("{}".format(d+second_double))
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + second_string)  