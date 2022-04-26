class Knowledge_base():
    def __init__(self):
        self.beliefs = []
    
    def add(self, belief):
        self.beliefs.append(belief)


    def print_self(self):
        for belief in self.beliefs:
                print(belief)
