def greet(name):
    print(f"Hello {name}")
    greet2(name)
    print("Getting ready to say bye")
    bye()

def greet2(name):
    print(f"Hello {name} how are you?")

def bye():
    print("Bye")

greet("John")