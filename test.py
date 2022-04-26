from sympy import Symbol
from sympy.logic.boolalg import *
from agent import Entail

from knowledge_base import Knowledge_base

p = Symbol('P')
q = Symbol('Q')
r = Symbol('R')

kb = Knowledge_base()
kb.add(Implies(Not(p), q))

kb.print_self()

sentence = And(q, p)

print(sentence)

result = Entail(kb, sentence)
print(result)

a = Symbol('A')

sentence = And(p,a)

print(sentence)

result = Entail(kb, sentence)
print(result)