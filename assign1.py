def addition(func):
    def wrapper(*args):
        func(*args)
        print("Addition")
        print(args[0] + args[1])
    return wrapper

@addition
def age(a, b):
    print("Ages are:")
    print(a)
    print(b)

def main():
    age(10, 20)

if __name__ == "__main__":
    main()