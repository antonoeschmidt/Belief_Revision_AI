import itertools
import regex
import sympy
from knowledge_base import Knowledge_base
import re


class Agent():
    def __init__(self,kb: Knowledge_base):
        self.t = 0
        self.kb = kb
       

    def __call__(self, percept):
        self.tell(self.kb,self.make_percept_sentence(percept,self.t))
        action = self.ask(self.kb,self.make_action_query(self.t))
        self.tell(self.kb,self.make_action_Sentence(action,self.t))
        self.t += 1
        return action
    
    def tell(self,kb: Knowledge_base, percept_sentence):
        
        pass
    
    def ask(self, kb: Knowledge_base, action_query):
        pass
    
    def make_percept_sentence(self):
        pass

    def make_action_query(self, t):
        pass

    def make_action_Sentence(self,action,t):
        pass
    

def splitOperation(clauses, opterator):
    result = []

    def split(clauses):
        for claus in clauses:
            if isinstance(claus, opterator):
                split(claus.args)
            else:
                result.append(claus)

    split(clauses)
    return result

def Entail(kb: Knowledge_base, sentence: sympy.logic.boolalg.BooleanFunction):
        clauses = kb.beliefs + [sympy.Not(sentence)]
        for i, claus in enumerate(clauses):
            clauses[i] = sympy.to_cnf(claus)

        clauses = splitOperation(clauses, sympy.And)
        new = set()
        while 1:
            pairs = list(itertools.combinations(clauses,2))
            clauses = set(clauses)
            for pair in pairs:
                resolvents = Resolve(pair[0],pair[1])
                if False in resolvents:
                    return True
                new = new.union(resolvents)

            if new.issubset(clauses):
                return False
            clauses = clauses.union(new)

def Resolve(ci: sympy.logic.boolalg.BooleanFunction, cj: sympy.logic.boolalg.BooleanFunction):
    arg_list = list( dict.fromkeys(Args(ci) + Args(cj)))
    output = []
    for arg in Args(ci):
        for arg2 in Args(cj):
            if arg == sympy.Not(arg2):
                # The code for Comprehension is based on the information on:
                #  https://stackoverflow.com/questions/21682804/pop-remove-items-out-of-a-python-tuple 
                resolvent = [x for x in arg_list if x != arg and x != arg2]
                output.append(sympy.Or(*resolvent))

    return output

def Args(clause: sympy.logic.boolalg.BooleanFunction):
    output = []
    args = str(clause).split('|')
    negated = False
    regex = "^[aA-zZ]"
    for set in args:
        for symbol in set:
            
            if symbol == '~':
                negated = True
                continue
            elif re.search(regex,symbol):
                if negated:
                    output.append(sympy.Not(sympy.Symbol(symbol)))
                else:
                    output.append(sympy.Symbol(symbol))
            negated = False
            
        
    return output
