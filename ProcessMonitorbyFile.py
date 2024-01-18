import os
import psutil
import time
from sys import *
import os

def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    separator = "*"*80
    log_path = os.path.join(log_dir,"MarvellousLog%s.Log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separtor="\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime()+"\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.os.dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except(psutil.NoSuchprocess,psutil,AccessDenied,psutil.ZombieProcess):
            pass

    for elements in listprocess:
        f.write("%s\n" % elements)

def main():
    print("-------------Marvellous Infosystem by Piyush Khairnar-------------")

    print("Application Name: ",argv[0])

    if(len(argv)!=2):
        print("Error : Invalid Number of arguments")
        exit()
    
    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This Script is used log reccord for running processes")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):    
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__=="__main__":
    main()























 







