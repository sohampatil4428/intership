# # Return statement
# # Treating a function as a value

# # def add2numbers(a,b):
# #     return (a + b)

# # def evenOdd(a):
# #     if(a % 2 == 0):
# #         return True
# #     return False

# # a = add2numbers(3,4)
# # print(a)
# # evenOdd(a)


# # Python Files
# # Directory and Files Management
# # "os" module

# # import os
# # Get current directory
# # print(os.getcwd())

# # Change directory
# # os.chdir("E:\\Code\\Lectures")
# # print(os.getcwd())

# # List directory and files
# # print(os.listdir())

# # # Make new directory
# # os.mkdir("DEMO")
# # print(os.listdir())

# # Change the name of directory
# # os.rename("DEMO","demo_test")

# # Remove directory
# # os.rmdir("demo_test")


# # CSV
# # import csv

# # Read CSV file
# # with open('demo.csv', 'r') as file:
# #     data = csv.reader(file)

# #     for line in data:
# #         print(line)

# # Write to CSV files
# # with open('emp.csv', 'a', newline='\n') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["ID", "Name", "Email"])
# #     writer.writerow([1,"Raju","raju@gmail.com"])
# #     writer.writerow([2,"Raju","raju@gmail.com"])
# #     writer.writerow([3,"Raju","raju@gmail.com"])


# # Exceptions
# # try
# # except
# # finally
# # else

# # Built-ins
# # print(dir(locals()['__builtins__']))

# try:
#     a = 5
#     print(a)

#     # print(a / 0)
#     del a
#     # print(a)
# except NameError:
#     print("Variable not defined error")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except:
#     print("Error")
# else:
#     print("Logic implemented successfully")
# finally:
#     print("Progarm Exceuted")

# print("Other codes")


print("------------------------------------------------------------------------------------------------------")

# def sumtwono(a,b):
#     print(a+b)
#     print(a-b)
# sumtwono(10,20)
# print("====")



#import os

#Get current directory
#print(os.getcwd())

#os.chdir("c:\Users\hp")
#print(os.getcwd())


#print(os.listdir())

#os.mkdir("new")
#print(os.listdir())


# os.rmdir("DEMO")
# print(os.listdir())


# os.remove("new")
# print(os.listdir())

import csv 

with open('new_data', 'r') as file:
    data = csv.reader(file)



