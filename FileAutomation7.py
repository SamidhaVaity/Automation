from sys import *
import os
import time

def DirectoryTravel(DirName, name):
    print("WE are going to scan the Directory : ", DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if (exist==True):
        for foldername, subfoldername, filename in os.walk(DirName):            
            for fname in filename:
                if(fname == name):
                    print("File is present in the directory with name:",fname)
    else:
        print("Invalid Path")           
            

def main():
    print("----------Automation Script-----------------")

    print("Automation Script Name: ",argv[0])
    if(len(argv) !=3):
        print("Invalid number of arguments")
        exit()

    
    if(argv[1]=="-h" or argv[1]=="H"): # Flag for display help
        print("This automation script is used to perform File Automations")
        exit()

    
    elif (argv[1]=="-u" or argv[1]=="-U"):    # Flag for displaying usage
        print("Usage : Name_of_Script First_Argument second Argument")
        print("Example: Demo.py Marvellous")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1],argv[2])
        endtime = time.time()

        print("Time taken to travel is :",endtime-starttime)

      
    

if __name__=="__main__":
    main()