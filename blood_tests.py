def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9" :
            return
        elif choice == "1":
            HDL_driver()

def HDL_driver():
    HDL = get_HDL_input()
    analysis = analyze_HDL(HDL)
    output_HDL(HDL,analysis)
    
    
def get_HDL_input():
    #get data
    print("Check HDL")
    level = input("Enter HDL level: ")
    level = int(level)
    return level

def analyze_HDL(level):
    #analyze data
    if level < 40 :
        return "Low"
    elif 40 <= level < 60 :
        return "Borderline Low"
    else :
        return "High"

def output_HDL(HDL, analysis):
    print("The HDL entered was {}".format(HDL))
    print("The level is {}".format(analysis))
    #output data

interface()

