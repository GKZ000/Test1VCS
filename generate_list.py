import random
def generation_list():
        alist = [x for x in range (random.randint(-10,10))]
        return alist

"""
print a generation_list
"""

def printIt()
    print(generation_list())
    
def main():
    printIt()

"""
If this script file is called, it will run main() directly
"""

if __name__ == '__main__':
    print("Test printIt():")
    main()
