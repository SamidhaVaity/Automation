from sys import *

def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("----------Automation Script-----------------")

    print("Automation Script Name: ",argv[0])

    if (len(argv)==2):
        if(argv[1]=="-h" or argv[1]=="H"): # Flag for display help
            print("This automation script is used to perform addition of two numbers")
            exit()

    
        elif (argv[1]=="-u" or argv[1]=="-U"):    # Flag for displaying usage
            print("Usage : Name_of_Script First_Argument Second_Argument")
            print("Example: Demo.py 11 10")
            exit()

        else:
            print("There is no such option to handle")

    if(len(argv) !=3):
        print("Invalid number of arguments")
        exit()
    else:
        Ret = Addition(int(argv[1]) , int(argv[2]))
        print("Addition is:", Ret)

if __name__=="__main__":
    main()