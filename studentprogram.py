import studentclass as sc

studentid = 1001
name = 'Lindsey'
dob = '06/12/2001'
classification = 'junior'

lindsey = sc.Student(studentid,name,dob,classification)

lindsey.calc_age()
lindsey.register()

print("Age is:", lindsey.get_age())
print("Student can register between:", lindsey.get_registration)
