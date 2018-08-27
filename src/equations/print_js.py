def printJS(name, exp, withJSDeclaration=True):
    import re
    s = str(exp)
    s = re.sub(r"\(t\)", "", s)
    s = re.sub(r"Derivative\((\w+), t\)", r"\1Dot", s)
    s = re.sub(r"Derivative\((\w+), \(t, 2\)\)", r"\1DotDot", s)
    s = re.sub(r"theta", u"\u03B8", s)
    name = re.sub(r"theta", u"\u03B8", name)
    if withJSDeclaration:
        s = u'const ' + name + u' = ' + s;
    else:
        s = name + u': ' + s;
    print(s.encode('utf-8'))
