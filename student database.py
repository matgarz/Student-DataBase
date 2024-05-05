"""
Mateo Fernando Garzon Velasco 2110011
420-LCU Computer Programming, Section 03
S. Hilal, instructor
Assignment 4
"""
#functions for G and LG
def gr(r):
    """returns the total grade of a student"""
    return sum(r[2:])
def gr_c(r):
    """returns the total grade of a student"""
    return sum(r[3:])
def lgr(r):
    """returns the letter grade of a student"""
    y = r[-1]
    if y < 65:
        return 'F'
    elif 65 <= y <= 74:
        return 'C'
    elif 75<= y <= 86:
        return 'B'
    elif y > 86:
        return 'A'
#dictionaries and lists
S= {}
record_list = []
record_c = [] #useful copy
Keys=['name','prg','T1','T2','A1','A2','A3','P','G','LG']
student_ids = []
#reading the file
fp = open('bro.txt')
x = fp.readlines()
for line in x:
    record_c.append(line.strip('\n').split(','))
    record_list.append(line.strip('\n').split(','))#creating a matrix of records
for record in record_list:
    student_ids.append(record[1])#creating the student id list
    record.pop(1)#deleting student ids from records
    for char in range(len(record)):
        if record[char].isdigit():
            record[char] = int(record[char])#making grades integers
    record.append(gr(record))#adding G to records
    record.append(lgr(record))#adding LG to records
#students dictionary
for record in range(len(record_list)):
    S[student_ids[record]] = dict(zip(Keys,record_list[record]))#creating students dictionary
programs = {}
#program dictionary
for info in S.values():           
    programs[info['prg']] = programs.get(info['prg'],0) + 1#creaing programs mini dictionary
#class stats dictionary
cl_stats = {}
cl_gr = []
#getting the class average
for val in S.values():
    cl_gr.append(val["G"])
cl_avg = '{:4.4g}'.format(sum(cl_gr)/len(cl_gr))
#number ofstudents
x = len(student_ids)
#getting the class median
cl_gr_s = sorted(cl_gr)
for i in range(len(cl_gr_s)):
    if not len(cl_gr_s)%2:
        if len(cl_gr_s[:i]) == len(cl_gr_s[i:]):
            cl_med = cl_gr_s[i]
    elif len(cl_gr_s)%2:
        if len(cl_gr_s[:i]) == len(cl_gr_s[i+1:]):
            cl_med = (cl_gr_s[i] + cl_gr_s[i-1])/2
#making the class mode
grs = {}
for k in S.values():
    grs[k['G']] = grs.get(k['G'],0) + 1
repetitions = sorted(grs.values())
mod_n = max(repetitions)
cl_mod_l= []
for score in grs:
    if grs[score] == mod_n:
        cl_mod_l.append(str(score))
cl_mod = ",".join(cl_mod_l)
#making the stats dictionary
cl_stats["Number of students"]= x
cl_stats["class average"] = cl_avg
cl_stats["class median"] = cl_med                           
cl_stats["class mode"] = cl_mod
#making a dictionary for the adventure
for record in record_c:
    for char in range(len(record)):
        if record[char].isdigit():
            record[char] = int(record[char])#making grades integers
    record.append(gr_c(record))#adding G to records
    record.append(lgr(record))#adding LG to records
HH_l = []
HP_l = []
H2_l = []
B2_l = []
B1_l = []
for i in record_c:
    if 'HH' in i:
        HH_l.append(i)
    elif 'HP' in i:
        HP_l.append(i)
    elif 'H2' in i:
        
        H2_l.append(i)
    elif 'B2' in i:
        B2_l.append(i)
    elif 'B1' in i:
        B1_l.append(i)
for i in range(len(HH_l)):
    for j in range(7):
        HH_l[i].pop(2)
for i in range(len(HP_l)):
    for j in range(7):
        HP_l[i].pop(2)
for i in range(len(H2_l)):
    for j in range(7):
        H2_l[i].pop(2)
for i in range(len(B2_l)):
    for j in range(7):
        B2_l[i].pop(2)
for i in range(len(B1_l)):
    for j in range(7):
        B1_l[i].pop(2)
master_l = [HH_l, HP_l, B2_l, B1_l, H2_l]
#programs with 3 or more
pro_3 = {}
for i in programs:
    if programs[i] > 2:
        pro_3.update({i:programs[i]})
#LG dictionary
LG_d = {}
for lol in S.values():           
    LG_d[lol['LG']] = LG_d.get(lol['LG'],0) + 1 
menu = """
1- How many different students are there? 
2- How many different programs are there? 
3- What program has the most number of students? 
4- Display class statistics: number of students, class average, mean and median based on total grade.
5- Display all the students in a particular program 
6- List all the programs that have 3 or more students enrolled. 
7- Print the full record for a given student. 
8- Display a pie chart plot to show the distribution of students among the different programs.
9- Display a bar chart to display the letter grade distributions.
10- Exit

"""
while True:
    print(menu)
    x = int(input("Enter your option:"))
    if x == 1:
        for i,stu in enumerate(S.values()):
            print(i+1,'\t',stu['name'],'\t',stu['prg'],'\t',stu['T1'],'\t',stu['T2'],'\t',stu['A1'],'\t',stu['A2'],'\t',stu['A3'],'\t',stu['P'],'\t',stu['G'],'\t',stu['LG'])
    elif x == 2:
        for i in enumerate(programs):
            print(str(i[0] + 1)+'.   ' + str(i[1]) + ":   ", programs[i[1]])
    elif x == 3:
        print(max(programs,key=programs.get), "with" ,str(max(programs.values())),"students.")
    elif x == 4:
        for j in cl_stats:
            print('{:20.20s}: {:10.10s}'.format(str(j),str(cl_stats[j])))
            #print(str(j)+ ":  " + str(cl_stats[j]))
    elif x == 5:
        t = input("Enter a program:")
        if t == 'HH':
            p = 0
        elif t == 'HP':
            p = 1
        elif t == 'B2':
            p = 2
        elif t == 'B1':
            p = 3
        elif t == 'H2':
            p = 4
            
        for k in master_l[p]:
            print(str(k[0]),'\t',str(k[1]),'\t',str(k[2]),'\t',str(k[3]))
    elif x == 6:
        for i in pro_3:
            print(str(i)+':'+str(pro_3[i]))
    elif x == 7:
        i_d= input("Enter student ID:")
        for key in S[i_d]:
            print('{:5.5s}: {}'.format(str(key),str(S[i_d][key])))
            #print(str(key),':','\t',str(S[i_d][key]))
    elif x == 8:
        import matplotlib
        import matplotlib.pyplot as pl
        labels = list(programs.keys())
        colors = ["blue", 'yellow', 'green', 'orange', 'red', 'purple', 'grey']
        sizes = list(programs.values())
        pl.pie(sizes, labels = labels, colors=colors, startangle=90, autopct='%1.1f%%')
        pl.axis('equal')
        pl.title('Program Distribution for Students')
        pl.show()
    elif x == 9:
        import numpy as np
        import matplotlib.pyplot as plt
        grades = list(LG_d.keys())
        markings = np.arange(len(grades))
        distribution = list(LG_d.values())
        plt.bar(markings,distribution, align='center',alpha=0.3)
        plt.xticks(markings,grades) #x axis markings
        plt.title("student grades")
        plt.xlabel("Grades")
        plt.ylabel("distribution") 
        plt.show()
        continue     
    elif x == 10:
        print("you are now exiting...")
        break


    
        
