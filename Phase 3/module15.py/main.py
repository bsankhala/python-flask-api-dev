import random
import math

from marks import calculate_total_and_percentage
from grade import get_grade
from utils import display_student_details

name = input("Enter student name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

student_id = random.randint(1000, 9999)

total, percentage = calculate_total_and_percentage(m1, m2, m3)

percentage = math.floor(percentage * 100) / 100

grade = get_grade(percentage)

display_student_details(name, student_id, total, percentage, grade)
