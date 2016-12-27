"""Class Inheritance:
Create Person as super class with name, age.
Create another two sub classes(student, teacher) for Person class;
Student parameters: name:age:class:marks. Methods: get_marks(), get_class.
Teacher parameters: name:age:Subj:Sal. add methods get_sub, get_sal."""

class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
class student(person):
	def __init__(self,classs,marks):
		self.classs=classs
		self.marks=marks
	def get_marks(self):
		return self.marks
	def get_class(self):
		return self.classs
		
class teacher(person):
	def __init__(self,sub,sal):
		self.sub=sub
		self.sal=sal
	def get_sub(self):
		return self.sub
	def get_sal(self):
		return self.sal
x = person("prasanna", 22)
y = student(10,25)
z=teacher("chemistry",20000)
print y.get_marks()
print y.get_class()
print z.get_sub()
print z.get_sal()


