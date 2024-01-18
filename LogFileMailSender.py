import os
import time
import psutil
import  urllib.request
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def us_connected():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=2)
        return True
    except urllib.request.URLError as err:
        return False

def MailSender(filename,time):
    try:
        fromaddr = "samidhavaity@gmail.com"
        email_password = "zxnszhgryezenbua"
        toaddt = "samidhav03@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystems.
        Please find attached document which contains Log of Running process.
        Log file is created at : %s    

        This is auto gennerated mail.

        Thanks & Regards,
        Samidha Narendra Vaity
        Marvellous Infosystems
        """%(toaddr,time)

        Subject = """
        Marvellous Infosystems Process log generated at : %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))

        attachment = open(filename,"rb")

        p = MIMEBase('application','octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)  

        s.starttls()

        s.login(fromaddr,email_password)    

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file successfully sent through Mail")

    except Exception as E:
        print("Enable to Send through Mail",E)

def ProcessLog(log_dir = 'Marvellous'):

    flag = os.path.isabs(log_dir)

    if flag == False:
        lod_dir = os.path.abspath(log_dir)

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    listprocess = []

    separator = "-"*80
    log_path = os.path.join(log_dir,"TimeLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystem Process Logger :"+time.ctime()+"\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocesss.append(pinfo);
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in lisprocess:
        f.write("%s\n"%element)

    print("Log filr is successfully generated at location %s"%(log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()

        print('Took %s second to send mail'%(endTime-startTime))
    else:
        print("There is no internet Connection")

def main():
    print("------------------Marvellous Infosystem--------------")

    print("Application name: ",argv[0])

    if(len(argv)!=2):
        print("Error : Invalid Number of arguments")
        exit()
    
    if(argv[1]=="-h" or argv[1]=="H"): 
        print("This automation script is used to log records of running processess")
        exit()

    
    if (argv[1]=="-u" or argv[1]=="-U"):    
        print("Usage : Application Name absolutepath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input",E)

if __name__=="__main__":
    main()





















