from dimod import ConstrainedQuadraticModel, CQM,  SampleSet
from dimod import Binary, quicksum 
from dwave.system import LeapHybridCQMSampler
import numpy as np


cqm = ConstrainedQuadraticModel()

totalNumberOfSloths = 4
numberOfDormitories = 2

c2 = [[0, 3, 4, 10], [3, 0, 2, 2], [4, 2, 0, 3], [10, 2, 3, 0]]
 
beds = [2, 2]


weight = [1, 1, 1, 1]

print(c2)

# Define x two dimensions variables 
# x i k == 1 if the product i will be handled by vehicle K
x = {
    (i, k): Binary('x{}_{}'.format(i, k))
    for i in range(totalNumberOfSloths) for k in range(numberOfDormitories)}


 


# We care about the objective function
objective = quicksum(c2[i][j] * x[(i,k)] * x[(j,k)] for i in range(totalNumberOfSloths) for j in range(totalNumberOfSloths) for k in range(numberOfDormitories))
cqm.set_objective(objective)

# We care about the constraints
for k in range(numberOfDormitories):
    cqm.add_constraint(quicksum(weight[i]*x[(i,k)] for i in range(totalNumberOfSloths)) <= beds[k])

for i in range(totalNumberOfSloths):
    cqm.add_constraint(quicksum(x[(i,k)] for k in range(numberOfDormitories)) == 1)

cqm_sampler = LeapHybridCQMSampler()
sampleset = cqm_sampler.sample_cqm(cqm)
# print(sampleset.info)

 
print(        sampleset )


