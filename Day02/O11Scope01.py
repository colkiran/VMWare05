
glbX = 100              # global variable

def fun(y):             # local variable
    global glbX         # do not assign any value
    print(f"y :{y}")
    glbX = 500          # local variable with same name as global
    print(f"glbX :{glbX}")

print(f"Before glbX :{glbX}")

fun(10)

print(f"After glbX :{glbX}")
