import numpy as np
# Importer methodes pour definir entre autres un modèle ISING
import dimod
# On importe les librairies de DWAVE
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Resolution du Max-Cut Problem sur une petite instance.

# On definit un group tres simple avec deux noeuds.
J = {(0,1):1}
h = {}

# On rentre le modele dans la structure associee.
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
# On affiche le modèle
print("Le modele resolu est le suivant :")
print(model)
print()

##                RESOLUTION EXACTE                ##
# On resout de maniere exact, sans recuit quantique
from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print("Resultat de la resolution exact (solution optimale)")
print(solution)
print()




# Or with *simulated annealing* (a heuristic method used in classical computers)

##                RESOLUTION APPROCHEE              ##
##     Recuit simule pour ordinateur classique      ##
sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("Solution obtenue par le recuit simule")
print(response)
print()


##                RESOLUTION APPROCHEE              ##
##     Recuit quantique sur Machine D-WAVE          ##
sampler = EmbeddingComposite(DWaveSampler())
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print("Solution obtenue par recuit quantique deploye sur machine DWAVE")
print(response)
print()
print()
print()
print()

