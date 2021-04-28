from random import randint
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite
# Déclaration des etudiants et projets
students = [0, 1, 2, 3, 4, 5, 6, 7, 8]
projects = [0, 1, 2]
 
size = len(students) * len(projects)
 
# Déclaration des arêtes
edges = []
 
o1 = -1000
o2 = 30
o3 = 10000
# Déclaration des poids et des aretes
w = {(0, 0): o1, (0, 1): o2, (0, 2): o3, (1, 2): o2, (1, 0): o3, (1, 1): o1, (2, 1): o1, (2, 0): o3, (2, 2): o2, (3, 0): o3, (3, 1): o2, (3, 2): o1, (4, 2): o2, (4, 1): o3, (4, 0): o1, (5, 1): o1, (5, 0): o3, (5, 2): o2, (6, 2): o3, (6, 1): o1, (6, 0): o2, (7, 0): o1, (7, 1): o3, (7, 2): o2, (8, 0): o3, (8, 2): o1, (8, 1): o2}
edges = [(0, 10), (0, 11), (1, 9), (1, 10), (2, 9), (2, 11), (3, 10), (3, 11), (4, 11), (4, 9), (5, 9), (5, 11), (6, 10), (6, 9), (7, 10), (7, 11), (8, 11), (8, 10)]
 
# Sumary choice 1
forMe = {0 : 1, 1 : 0, 2 : 0, 3 : 1, 4 : 2, 5 : 0, 6 : 1, 7 : 1, 8 : 0}
 
def get_index(student_index, project_index):
    return student_index * len(projects) + project_index
 
def get_student_and_project(index):
    return divmod(index,len(projects))
 
coeff = 1
lagrange_parameter_room = [3 * coeff, 4 * coeff, 2 * coeff]
 
lagrange_parameter_only_one = 100
 
 
Q = defaultdict(int)
 
# Objective function
for student_index in students:
    for project_index in projects:
        ind1 = get_index(student_index, project_index)
        Q[(ind1, ind1)] += w[(student_index, project_index)]
print(Q)
 
# Constraint 1 : Room per projects
for project_index in projects:
    for student_index in students:
        ind1 = get_index(student_index, project_index)
        Q[(ind1, ind1)] += lagrange_parameter_room[project_index]
 
print(Q)
 
for project_index in projects:
    for student_index in range(len(students)):
        for student_index_2 in range(student_index, len(students)):
            ind1 = get_index(student_index, project_index)
            ind2 = get_index(student_index_2, project_index)
            Q[(ind1, ind2)] += 0
 
print(Q)
 
# Constraint 2 : One project per student
for student_index in students:
    for project_index in projects:
        ind1 = get_index(student_index, project_index)
        Q[(ind1, ind1)] -= lagrange_parameter_only_one
 
for student_index in students:
    for project_index in projects:
        for project_index_2 in projects:
            ind1 = get_index(student_index, project_index)
            ind2 = get_index(student_index, project_index_2)
 
            Q[(ind1, ind2)] += lagrange_parameter_only_one
 
sampler = EmbeddingComposite(DWaveSampler())
results = sampler.sample_qubo(Q,num_reads=10000)
 
 
# Get the results
smpl = results.first.sample
energy = results.first.energy
print("Size ", size)
print("Energy ", energy)
 
 
print(results)
'''
# Check the results by doing the sums directly
# J sum
sum_j = 0
for i in range(size):
    for j in range(size):
        sum_j += J[i, j] * smpl[i] * smpl[j]
print("Checking Hard nurse constraint ", sum_j)
 
 
# workforce sum
sum_w = 0
for d in range(n_projects):
    sum_n = 0
    for n in range(n_students):
        sum_n += effort * smpl[get_index(n, d)]
    sum_w += lagrange_hard_shift * (sum_n - workforce) * (sum_n - workforce)
print("Checking Hard shift constraint ", sum_w)
 
 
# max_project
sum_f = 0
for n in range(len(students)):
    sum_d = 0
    for d in range(len(projects)):
        sum_d += preference * smpl[get_index(n, d)]
    sum_f += lagrange_soft_nurse * (sum_d - max_project_per_student) * (sum_d - max_project_per_student)
print("Checking Max project per student ", sum_f)
'''
# Graphics
sched = [get_student_and_project(j) for j in range(size) if smpl[j] == 1]
str_header_for_output = " " * 13
str_header_for_output += "  ".join(map(str, range(len(projects))))
print(str_header_for_output)
for n in range(len(students)):
    str_row = ""
    for d in range(len(projects)):
        outcome = "X" if (n, d) in sched else " "
        if d > 9:
            outcome += " "
        str_row += "  " + outcome
    print("Student ", n, str_row)
