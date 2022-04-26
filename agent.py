import itertools
import sympy
from knowledge_base import Knowledge_base


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
    
    
def Entail(kb: Knowledge_base, sentence: sympy.logic.boolalg.BooleanFunction):
        kb.add(sympy.Not(sentence))
        clauses = []
        for claus in kb.beliefs:
            clauses.append(sympy.to_cnf(claus))
        new = []
        pairs = list(itertools.combinations(clauses,2))
        while 1:
            for pair in pairs:
                resolvents = Resolve(pair[0],pair[1])
                if not resolvents:
                    return True
                new += (resolvents)

            if set(new).issubset(set(clauses)):
                return False
            clauses += new

            
        



def Resolve(ci: sympy.logic.boolalg.BooleanFunction, cj: sympy.logic.boolalg.BooleanFunction):
    output = ci.args + cj.args
    for arg in ci.args:
        for arg2 in cj.args:
            if arg == sympy.Not(arg2):
                # The code for Comprehension is based on the information on:
                #  https://stackoverflow.com/questions/21682804/pop-remove-items-out-of-a-python-tuple 
                output = [x for x in output if x != arg and x != arg2] 
    
    if output == ci.args + cj.args:
        return []
    return output
    

x = sympy.Symbol("x")
b = sympy.Symbol("b")
c = sympy.Symbol("c")
d = sympy.Symbol("d")
test = sympy.And(sympy.And(x,b),c)
test2 = sympy.And(sympy.And(d,sympy.Not(b)),sympy.Not(c))
kb = Knowledge_base()
kb.add(test)

print(Entail(kb,test2))
kb2 = Knowledge_base()
kb2.add(x)
print(Entail(kb2,b))
