def printJS(name, exp):
    import re
    s = str(exp)
    s = re.sub(r"\(t\)", "", s)
    s = re.sub(r"Derivative\(theta([0-9]), t\)", r"theta\1Dot", s)
    s = re.sub(r"Derivative\(theta([0-9]), \(t, 2\)\)", r"theta\1DotDot", s)
    s = re.sub(r"theta", u"\u03B8", s)
    name = re.sub(r"theta", u"\u03B8", name)
    res = u'const ' + name + u' = ' + s;
    print(res.encode('utf-8'))
