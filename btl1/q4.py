def square(x):
    return x*2

def increase(x):
    return x+1

def doublee(x):
    return x*2

def compose_recursive(*args):
    
    if len(args) == 1:
        return args[0]
    return lambda x: args[-1](compose_recursive(*args[:-1])(x))

print(compose_recursive(square, increase)(3))
