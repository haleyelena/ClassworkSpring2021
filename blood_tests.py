def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9" :
            return

def HDL_driver():
    #get data
    print("Check HDL")
    level = input("Enter HDL level: ")
    level = int(level)
    #analyze data
    if level < 40 :
        print("Low")
    elif level >= 40 | level < 60 :
        print("Borderline Low")
    else :
        print("High")
    #output data

HDL_driver()

