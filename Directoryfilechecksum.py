from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag=os.path.isabs(path)
    if flag ==False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs,filelist in os.walk(path):
            print("Current Folder is : ",dirName)
            for filen in filelist:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)        
                print (path)
                print(file_hash)
                print('')
    
    else:
        print("Invalid path")
    
    

def main():

    print("------Marvellous Infosystem by Piyush Khairnar----------")

    print("Application Name: ", (argv[0]))

    if (len(argv)!=2):
        print(" Error : Invalid numbers of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This Script is used to traverse specific directory")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage - ApplicationName AbsolutePath_of_Directory")
        exit()
    
    try:
        DisplayChecksum(argv[1])
    
    except ValueError:
        print("Error: Invalid data type of Input")
    
    except Exception as E:
        print("Error : Invalid Input",E)



if __name__=="__main__":
    main()