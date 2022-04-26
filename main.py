from regex import D
from sympy import to_cnf, SympifyError
from knowledge_base import Knowledge_base


if __name__ == '__main__':
    askinput = ">>> "
    operation = ''
    kb = Knowledge_base()
    while (operation != 'q'):
        print(
        f"""--- Options: ---
a to add belief
d to display Knowledge base
q to quit
        """)               
        operation = input(askinput)
       
        if(operation == 'a'):
            try:
                print("Write statement:")
                statement = input(askinput)
                statement = to_cnf(statement)
                print(statement)
                kb.add(statement)
            except SympifyError:
                print('Invalid Preposition')
        elif(operation == 'd'):
            kb.print_self()

        else:
            print("Please choose a valid option")