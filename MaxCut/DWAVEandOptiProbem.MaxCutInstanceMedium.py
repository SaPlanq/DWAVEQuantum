import numpy as np
# Importer methodes pour definir entre autres un modèle ISING
import dimod
# On importe les librairies de DWAVE
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Resolution du Max-Cut Problem sur une petite instance.

# On definit un graphe simple avec cinq noeuds.
J = {(0,1):1,(0,2):1,(1,2):1,(1,3):1,(2,4):1,(3,4):1}
h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
print("The model that we are going to solve is")
print(model)
print()

# On rentre le modele dans la structure associee.
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
# On affiche le modèle
print("Le modele resolu est le suivant :")
print(model)
print()


 


##                RESOLUTION APPROCHEE              ##
##     Recuit quantique sur Machine D-WAVE          ##
sampler = EmbeddingComposite(DWaveSampler(solver='Advantage_system4.1'))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print(response)
print()
print()
print()
print()



