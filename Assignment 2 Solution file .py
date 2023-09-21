#!/usr/bin/env python
# coding: utf-8

# Question 1: Complex Numbers 

# In[12]:


### Using the class and dunder operators 

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag == 0:
            return f"{self.real:.2f} + 0.00i"
        elif self.real == 0:
            return f"0.00 + {self.imag:.2f}i"
        elif self.imag < 0:
            return f"{self.real:.2f} - {abs(self.imag):.2f}i"
        else:
            return f"{self.real:.2f} + {self.imag:.2f}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        divisor = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / divisor
        imag_part = (self.imag * other.real - self.real * other.imag) / divisor
        return ComplexNumber(real_part, imag_part)

    def modulus(self):
        return (self.real**2 + self.imag**2)**0.5


if __name__ == "__main__":
    try:
        # Input Format: "real_part imag_part"
        c_real, c_imag = map(float, input("Enter the first complex number: ").split())
        d_real, d_imag = map(float, input("Enter the second complex number: ").split())

        c = ComplexNumber(c_real, c_imag)
        d = ComplexNumber(d_real, d_imag)

        print(c + d)
        print(c - d)
        print(c * d)
        print(c / d)
        print(f"{c.modulus():.2f}")
        print(f"{d.modulus():.2f}")

    except ValueError:
        print("Invalid input format. Please provide valid real and imaginary parts separated by a space.")


# Qustion 2 MRO 

# ![image.png](attachment:image.png)  ![image-2.png](attachment:image-2.png)

# In[10]:


# Base class1 - Object
class Object:
    def method(self):
        print("Method of Object")
    pass
        
# derived class2 - X
class X(Object):
    def method(self):
        print("Method of X")
    pass
# Derived Class2.1 - Y
class Y(Object):
    def method(self):
        print("Method of Y")
    pass   
# Derived Class2.2 - Z
class Z(Object):
    def method(self):
        print("Method of Z")
    pass
# Derived class3 A

class A(X,Y):
    def method(self):
        print("Method of A")        
    pass
# Derived class3.1 B

class B(Y,Z):
    def method(self):
        print("Method of B")        
    pass

objc = A()
objc.method()
print(A.mro())

objc1 = B()
objc1.method()
print(B.mro())
# Derived class4 M
'''
#If I crate the following class it gives TypeError: Cannot create a consistent method resolution order (MRO) for bases Z, A, B
#class M(Z,A,B):
    #def method(self):
        #print("Method of M")        
    #pass
#objc2 = B()
#objc2.method()
#print(M.mro())
''' 
class M(A,B,Z):
    def method(self):
        print("Method of M")        
    pass
objc2 = B()
objc2.method()
print(M.mro())


# In[13]:


# Base class1
class A:
    def method(self):
        print("Method of A")
    pass
        
# Base class2
class B(A):
    def method(self):
        print("Method of B")
    pass
        
# Derived class
''' This gives Cannot create a consistent method resolution
order (MRO) for bases A, B
class C(A, B):
    def method(self):
        print("Method of C")        
    pass

objc = C()
objc.method()
'''
class C(B,A):
    def method(self):
        print("Method of C")        
    pass

objc = C()
objc.method()
print(C.mro())


# Qustion 3: Bank account 

# Create a BankAccount class for customers with amount and name.
# It should have the following functionalities:
# •	Display balance amount with account holder’s name
# •	Deposit an amount to the account and display the balance
# •	Withdraw an amount from the account. While withdrawing check if the transaction is viable with sufficient balance in the account.
# •	If the transaction is not viable then raise an exception, that transaction cannot be processed
# •	Transfer an amount from one account to another. Display the balance for each account on successful transfer between the parties. During this process check for the viability of the transaction (sufficient balance) and report an error if transfer is interrupted. If the transaction is possible, then debit from sender and credit amount in receiver’s account.
# 

# In[14]:


class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display_balance(self):
        print(f"Account Holder: {self.name}, Balance: ${self.amount}")

    def deposit(self, amount):
        self.amount += amount
        print(f"Deposited ${amount} into {self.name}'s account. New balance for {self.name}: ${self.amount}")

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            print(f"Withdrew ${amount} from {self.name}'s account. New balance for {self.name}: ${self.amount}")
        else:
            raise BalanceException("Insufficient balance. Transaction cannot be processed.")

    def transfer(self, other_account, amount):
        try:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"Transferred ${amount} from {self.name}'s account to {other_account.name}'s account.")
            print(f"New balance for {self.name}: ${self.amount}, New balance for {other_account.name}: ${other_account.amount}")
        except BalanceException as e:
            print(f"Transfer failed. Reason: {e}")


class InterestRewardAcc(BankAccount):
    def __init__(self, name, amount):
        super().__init__(name, amount)

    def deposit(self, amount):
        interest = amount * 0.05
        self.amount += amount + interest
        print(f"Deposited ${amount} into {self.name}'s InterestRewardAcc account with 5% interest.")
        print(f"New balance for {self.name}: ${self.amount}")


class SavingsAcc(InterestRewardAcc):
    def __init__(self, name, amount):
        super().__init__(name, amount)

    def withdraw(self, amount):
        service_fee = 5
        total_withdrawal = amount + service_fee
        if total_withdrawal <= self.amount:
            self.amount -= total_withdrawal
            print(f"Withdrew ${amount} from {self.name}'s SavingsAcc account with a service fee of ${service_fee}.")
            print(f"New balance for {self.name}: ${self.amount}")
        else:
            raise BalanceException("Insufficient balance. Transaction cannot be processed.")


# Example usage
emily_account = BankAccount("Emily", 1000)
sara_account = BankAccount("Sara", 2000)

emily_account.display_balance()
sara_account.display_balance()

emily_account.deposit(100)
sara_account.withdraw(500)
emily_account.transfer(sara_account, 200)

kevin_account = InterestRewardAcc("Kevin", 1000)
kevin_account.deposit(100)

john_account = SavingsAcc("John", 1000)
john_account.deposit(100)
john_account.transfer(sara_account, 500)


# Qustion 4 : Intraactive Calculator 
#     

# In[1]:


class FormulaError(Exception):
    pass

def calculate_result(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise FormulaError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise FormulaError("Invalid operator.")

def validate_input(input_str):
    elements = input_str.split()
    if len(elements) != 3:
        raise FormulaError("Invalid formula format. Please enter a formula like '1 + 1'.")
    
    try:
        num1 = float(elements[0])
        num2 = float(elements[2])
    except ValueError:
        raise FormulaError("Invalid number format. Please enter valid numbers.")
    
    operator = elements[1]
    if operator not in ['+', '-', '*', '/']:
        raise FormulaError("Invalid operator. Only +, -, *, and / are allowed.")
    
    return num1, operator, num2

def main():
    while True:
        user_input = input("Enter a formula (e.g., 1 + 1) or type 'quit' to exit: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        try:
            num1, operator, num2 = validate_input(user_input)
            result = calculate_result(num1, operator, num2)
            print("Result:", result)
        except FormulaError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()


# In[ ]:




