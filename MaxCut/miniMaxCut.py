import numpy as np
# Importer methodes pour definir entre autres un modèle ISING
import dimod
# On importe les librairies de DWAVE
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Resolution du Max-Cut Problem sur une petite instance.

# On definit un group tres simple avec deux noeuds.
# J correspond aux expressions quadratiques
# (var1, var2):poids
J = {(1,2):1, (2,3):1, (3,4):1, (1,4):1, (4,5):1, (3,5):1, (4,6):1, (5,6):1}
# poids de chaque qubits pris individuellement
h = {}

# On rentre le modele dans la structure associee.
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
# On affiche le modèle
print("Le modele resolu est le suivant :")
print(model)


##                RESOLUTION APPROCHEE              ##
##     Recuit quantique sur Machine D-WAVE          ##
sampler = EmbeddingComposite(DWaveSampler())
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print(response)
 
