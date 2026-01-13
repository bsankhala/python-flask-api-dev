from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def view_dashboard(self):
        pass


class Student(User):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.__wallet_balance = 0         
        self.enrolled_courses = []

    def get_wallet_balance(self):
        return self.__wallet_balance

    def add_funds(self, amount):
        if amount > 0:
            self.__wallet_balance += amount

    def _deduct_balance(self, amount):
        if self.__wallet_balance >= amount:
            self.__wallet_balance -= amount
            return True
        return False

    def view_dashboard(self):
        print(f"\nStudent Dashboard: {self.name}")
        print("Enrolled Courses:")
        for course in self.enrolled_courses:
            print("-", course.title)


class Instructor(User):

    def __init__(self, name, email):
        super().__init__(name, email)
        self.created_courses = []

    def view_dashboard(self):
        print(f"\nInstructor Dashboard: {self.name}")
        print("Created Courses:")
        for course in self.created_courses:
            print("-", course.title)


class Course:

    def __init__(self, title, instructor, price):
        self.title = title
        self.instructor = instructor
        self.price = price


    def enroll(self, student):
        print("Base course enroll called")


class FreeCourse(Course):

    def __init__(self, title, instructor):
        super().__init__(title, instructor, price=0)

    def enroll(self, student):
        student.enrolled_courses.append(self)
        print(f"{student.name} enrolled in FREE course '{self.title}'")


class PaidCourse(Course):

    def __init__(self, title, instructor, price, discount=0):
        super().__init__(title, instructor, price)
        self.discount = discount

    def enroll(self, student):
        final_price = self.price - self.discount
        if student._deduct_balance(final_price):
            student.enrolled_courses.append(self)
            print(f"{student.name} enrolled in PAID course '{self.title}' for {final_price}")
        else:
            print("Insufficient wallet balance!")


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class WalletPayment(Payment):

    def __init__(self, student):
        self.student = student

    def process_payment(self, amount):
        if self.student._deduct_balance(amount):
            print("Wallet payment successful!")
        else:
            print("Wallet payment failed – insufficient balance")


class CardPayment(Payment):

    def process_payment(self, amount):
        print(f"Card charged ₹{amount}. Payment successful")


if __name__ == "__main__":

    s1 = Student("Aarav", "aarav@gmail.com")
    i1 = Instructor("Dr. Mehta", "mehta@gmail.com")

    s1.add_funds(500)
    print("Wallet Balance:", s1.get_wallet_balance())

    c1 = FreeCourse("Python Basics", i1)
    c2 = PaidCourse("Data Science Pro", i1, price=400, discount=50)

    i1.created_courses.extend([c1, c2])

    c1.enroll(s1)    
    c2.enroll(s1)   

    wallet_pay = WalletPayment(s1)
    wallet_pay.process_payment(100)

    card_pay = CardPayment()
    card_pay.process_payment(200)

    # dashboards
    s1.view_dashboard()
    i1.view_dashboard()
