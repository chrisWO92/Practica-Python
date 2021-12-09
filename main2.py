from a import A
from b import B
from c import C

def main():
    a = A()
    b = B()
    c = C()
    
    a.a()
    a.b()
    b.b()
    
    c.a()
    c.b()
    c.c()
    
if __name__ == "__main__":
    main()