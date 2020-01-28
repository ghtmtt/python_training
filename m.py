class Employee:

    def __init__(self, name, paycheck):
        self.name = name
        self.paycheck = paycheck

    def print_attributes(self):
        print('The name of the Employee is {self.name} and the paycheck is {self.paycheck}')

    def raise_paycheck(self, n):
        if n > 1:
            raise Exception(f'n must be expessed as %')
        self.paycheck = self.paycheck + (self.paycheck * n)