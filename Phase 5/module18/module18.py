class Student:

    school_name = "ABC School"

    def __init__(self, roll_no, name, marks):
        if len(marks) != 5:
            raise ValueError("Marks must be exactly of 5 subjects")

        for i in range(5):
            if marks[i] > 100 or marks[i] < 0:
                raise ValueError("Marks should be between 0 and 100")

        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calc_perc(self):
        total = self.calculate_total()
        return total / 5

    def display(self):
        print("\nSchool:", Student.school_name)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calc_perc())

s1 = Student(1, "Raj", [76, 87, 65, 92, 80])
s2 = Student(2, "Priya", [88, 79, 91, 84, 77])
s3 = Student(3, "Amit", [67, 72, 81, 69, 74])


s1.display()
s2.display()
s3.display()