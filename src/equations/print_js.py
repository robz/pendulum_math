import sympy

def printJS(name, exp, withJSDeclaration=True):
    print('const ')
    sympy.print_jscode(exp, assign_to=name, user_functions=[
        ("sin", "sin"),
        ("cos", "cos"),
    ])
    print(';')
