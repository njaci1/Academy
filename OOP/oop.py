class Employee:
    num_emps = 0
    raise_mnt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #elf.pay = pay
        self.email = first + '.' + last + '@test.com'

        Employee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print (emp_1.email)
print (emp_1.fullname())









