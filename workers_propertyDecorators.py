class Workers:
    def __init__(self, firstName, lastName):
        self.firstName = firstName,
        self.lastName = lastName,

    @property
    def email(self):
        return '{}.{}@gmail.com' .format(self.firstName, self.lastName)
    
    @property
    def fullName(self):
        return '{} {}' .format(self.firstName, self.lastName)

    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName

    @fullName.deleter
    def fullName(self):
        print('Delete name!')
        self.firstName = None
        self.lastName = None

emp_1 = Workers('Jerry', 'Freedom')

emp_1.fullName = 'John Wick'

print(emp_1.firstName)
#print(emp_1.email)
print(emp_1.fullName)

del emp_1.fullName
