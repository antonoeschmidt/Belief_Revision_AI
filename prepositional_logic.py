# This code is taken and modified from https://dev.to/pars3c/mathematical-notation-for-python-developers-propositional-logic-2dkn
# Date accessed: 12/004/2022


# |1 ∧ 0 = 0|0 ∧ 1 = 0|1 ∧ 1 = 1 |0 ∧ 0 = 0|
def AND(a,b):
    return (a and b)

# |1 ∨ 0 = 1|0 ∨ 1 = 1|1 ∨ 1 = 1|0 ∨ 0 = 0|
def OR(a,b):
    return (a or b) 

# If a = 1 then ~a = 0 or vice versa
def NOT(a):
    return not(a)

# |0 → 0 = 1| 0 → 1 = 1|1 → 1 = 1|1 → 0 = 0|
def IMPLIES(a,b):
    if a:
        return b
    return True

# |0 ↔ 0 = 1| 0 ↔ 1 = 0|1 ↔ 1 = 1|1 ↔ 0 = 0|
def IFF(a,b):
    return AND(IMPLIES(a,b),IMPLIES(b,a))

# |1 ⊻ 0 = 1| 0 ⊻ 1= 1|1 ⊻ 1= 0| 0 ⊻ 0 = 0|
def XOR(a,b):
    return NOT(IFF(a,b))


