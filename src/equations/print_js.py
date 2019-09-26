import sympy


def printJS(name, exp):
    print("const", sympy.jscode(
            exp, assign_to=name, user_functions=[("sin", "sin"), ("cos", "cos")]
        )
    )
