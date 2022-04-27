from sympy import Symbol
from sympy.logic.boolalg import *
from agent import Entail

from knowledge_base import Knowledge_base

## TODO use unittest?

p = Symbol('P')
q = Symbol('Q')
r = Symbol('R')
s = Symbol('S')

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



kb.add(Implies(q,p))
kb.add(Implies(p,And(r,s)))

sentence = And(p,r,s)

kb.print_self()

print('sentence', sentence)

result = Entail(kb, sentence)
print(result)

kb2 = Knowledge_base()
kb2.add(q)

print(Entail(kb2,s))