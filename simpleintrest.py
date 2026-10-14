import sys
def simple_interest(principal,interest,time):
    return (principal*interest*time)/100

if __name__ == "__main__":
    p = float(sys.avgv[1])
    r = float(sys.avgv[2])
    t = float(sys.avgv[3])
    
    print("Simple Interest = ",simple_interest(p,r,t))