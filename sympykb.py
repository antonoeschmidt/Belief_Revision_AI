from sympy.logic import *
from sympy import Symbol


rain = Symbol("rain")

hagrid = Symbol("hagrid")  

dumbledore = Symbol("dumpledore")  

knowledge_base = And(                   

   Implies(Not(rain), hagrid),

   Or(hagrid, dumbledore),

   Not(And(hagrid, dumbledore)),

   hagrid

)

print(knowledge_base)