# Python file one module

from file_two import function_three

print("File one __name__ is set to: {}" .format(__name__))


def function_one():
   print("Function one is executed")


def function_two():
   print("Function two is executed")


if __name__ == "__main__":
    print("file_one executed directly")
    function_one()
    function_three()

else:
    print("file_one executed while imported into another file")
