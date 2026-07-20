# class Student:
#     college_name = "STBG"
#     def __init__(self,fullname):
#         self.name = fullname
#        # print("adding new student")
#     def hello(self):
#         print("WELCOMNE")
#     def get_marks(self):
#         return
#          self.marks


# s1 = Student("Ram")
# s1.hello()
# print(s1.college_name)
# print(s1.get_marks)
# s2 = Student("rg")
# print(s2.name)

class Employee:
    def __init__(self, salary, id, name, department):
        self.salary = salary
        self.id = id
        self.name = name
        self.department = department

    def display(self):
        print(f"id: {self.id}, name: {self.name}, department: {self.department}, salary: {self.salary}")

    def get_salary(self):
        return self.salary

    def get_increment_salary(self):
        self.salary = self.salary + (10 * self.salary / 100)
        return self.salary


employee1 = Employee(100, 12, "Ram", "STBG")
employee1.display()
print("Salary:", employee1.get_salary())
#print(employee1._name)


employee1.get_increment_salary()
print("After 10% increment:", employee1.get_salary())
