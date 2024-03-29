from random import randint
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite
# cities
cities = [0, 1, 2, 3]
position = [0, 1, 2, 3]
size = len(cities)**2

# number of cities, edges and costs (distances)
n = 4
edges = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
cij = {(0, 0): 0, (0, 1): 10, (0, 2): 10, (0, 3): 14, (1, 0): 10, (1, 1): 0, (1, 2): 14, (1, 3): 10, (2, 0): 10, (2, 1): 14, (2, 2): 0, (2, 3): 10,(3, 0): 14, (3, 1): 10, (3, 2): 10, (3, 3): 0}

# we enlarge a dimension to take the position one to fit into the matrix. 
def get_index(city_index, position_index):
    return city_index * n + position_index
# reverse of the previous method
def get_city_and_position(index):
    return divmod(index,n)
 
 
#
# coeff = 1
# lagrange_parameter = [3 * coeff, 4 * coeff, 2 * coeff]
# lagrange_parameter_only_one = 100
#
 
Q = defaultdict(int)

# Objective function: sum of the distances
for city_i in cities:
    for city_j in cities:
        for position_t in position:
        
 
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
