numofstudents = int(raw_input('Enter No. of Students : '))
student = []
a = []
b = []
c = []
d = []
for i in range(0, numofstudents):
    x = {}
    x['Name'] = raw_input("Enter Student Name : ")
    x['Maths_Marks'] = int(raw_input("Enter Student Maths Marks : "))
    x['Science_Marks'] = int(raw_input("Enter Student Science Marks : "))
    x['Social_Marks'] = int(raw_input("Enter Student Social Marks : "))
    x['Total'] = x['Maths_Marks'] + x['Science_Marks'] + x['Social_Marks']
    student.append(x)
    print "Total Marks :", x['Total']
    a.append(x['Total'])
    b.append(x['Maths_Marks'])
    c.append(x['Science_Marks'])
    d.append(x['Social_Marks'])
print "Highest Total :", max(a)
print "Lowest Total :", min(a)
print "Highest Marks in Maths :", max(b)
print "Lowest Marks in maths:", min(b)
print "Highest Marks in Science:", max(c)
print "Lowest Marks in Science:", min(c)
print "Highest Marks in Social:", max(d)
print "Lowest Marks in Social:", min(d)
e = ''
for p in student:
    if p['Total'] == max(a):
        e += p['Name'] + ', '
print "Highest Total is", max(a), "by", e
f = ''
for q in student:
    if q['Total'] == min(a):
        f += q['Name'] + ', '
print "Lowest Total is", min(a), "by", f
g = ''
for r in student:
    if r['Maths_Marks'] == max(b):
        g += r['Name'] + ', '
print "Highest Marks in Maths are", max(b), "by", g
h = ''
for s in student:
    if s['Maths_Marks'] == min(b):
        h += s['Name'] + ', '
print "Lowest Marks in Maths are", min(b), "by", h
i = ''
for t in student:
    if t['Science_Marks'] == max(c):
        i += t['Name'] + ', '
print "Highest Marks in Science are", max(c), "by", i
j = ''
for u in student:
    if u['Science_Marks'] == min(c):
        j += u['Name'] + ', '
print "Lowest Marks in Science are", min(c), "by", j
k = ''
for v in student:
    if v['Social_Marks'] == max(d):
        k += v['Name'] + ', '
print "Highest Marks in Social are", max(d), "by", k
l = ''
for w in student:
    if w['Social_Marks'] == min(d):
        l += w['Name'] + ', '
print "Lowest Marks in Social are", min(d), "by", l
