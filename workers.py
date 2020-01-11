class Workers:

    paise_amt = 1.04

    def __init__ (self, firstName, lastName, pay):
        self.firstName = firstName,
        self.lastName = lastName,
        self.email = firstName + "." + lastName  + "@company.com",
        self.pay = pay

    def fullName(self):
        return '{} {}' .format(self.firstName, self.lastName) 

    def apply_raise(self):
        self.pay = int(self.pay * self.paise_amt)

    def __repr__(self):
        return "Workers '{}' '{}' '{}' ".format(self.firstName, self.lastName, self.pay)

    def __str__(self):
        return '{} - {}' .format(self.fullName(), self.email)

class Developer(Workers):
    paise_amt = 1.10

    def __init__ (self, firstName, lastName, pay, prog_lang):
        super().__init__(firstName, lastName, pay)
        self.prog_lang = prog_lang
            
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())

class Manager(Workers):
    def __init__ (self, firstName, lastName, pay, employees=None):
        super().__init__(firstName, lastName, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())

    


dev_1 = Developer('Jerry', 'Freedom', 50000, 'Python')
dev_2 = Developer('John', 'Wick', 60000, 'Asm')

mgr_1 = Manager('Tonny', 'Montana', 90000, [dev_1])

print(len(dev_1))

print(dev_1 + dev_2)       

#print(repr(dev_1))
#print(str(dev_1))

