# starts with {}
# def evenCheck(num):
#     print("I'm checking to see if {} is even!".format(num))
#
#     # Experienced way: (Don't need an if statement)
#     print("And I'm finding it's {}".format(num%2 == 0))
#
# evenCheck(41)
ints = [11,12,2,4,3,5,67,12,21,15,8,9,10]
# count = 0
def count_evens(nums):
  # CODE GOES HERE
  count = 0
  for i in ints:
      if i%2==0:
          count = count+1
  return count



# result = count_evens(ints)
# print(result)

# def hello(name='Jose'):
#     return 'Hello '+name

# def hello():
#     return 'Hi Jose!'
#
# def other(func):
#     print ('Other code would go here')
#     print (func())
#
# other(hello)

def new_decorator(func):

    def wrap_func():
        print ("Code would be here, before executing the func")

        func()

        print ("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print ("This function is in need of a Decorator")

func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
