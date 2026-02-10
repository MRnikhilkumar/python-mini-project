x = 155  # global variable 
def value():
    # x = 88   # local variable 
    print(x)
value()
value()


x = 155  # global variable 
def value():
    global x
    x = 88   # change global  variable 
    print(x)
value()
value()


