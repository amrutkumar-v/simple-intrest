def simple_interest(principal,interest,time):
    return (principal*interest*time)/100

if __name__ == "__main__":
    p = int(input("Enter Principal Amount: "))
    r = float(input("Enter Interest Rate: "))
    t = int(input("Enter Time (in years): "))
    
    print("Simple Interest = ",simple_interest(p,r,t))