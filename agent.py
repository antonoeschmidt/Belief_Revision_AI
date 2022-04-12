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