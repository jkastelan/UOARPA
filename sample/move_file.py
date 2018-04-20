#from paramiko import SSHClient
#from scp import SCPClient
import os
import logging
import sys
# Ensure you have run key-based authentication setup    
#ssh = SSHClient()
#ssh.load_systen_host_keys()
#with SCPClient(ssh.get_transport()) as scp:

#needs irigin file env variable ORGN
if os.getenv("ORGN") is None:
    print("needs env var ORGN")
    sys.exit()
            
if os.getenv("DSTN") is None:
    print("needs env var DSTN")    
    sys.exit()

if os.getenv('NMAX') is None:
    print ("needs NMAX")
    sys.exit()

def move_file():
    #counts files in current dir
    nfile = len(os.listdir(os.environ["ORGN"]))
    print (nfile)
    if nfile>0:  ## are there any files to move
        # take most recent file name
        firstfile = sorted(os.listdir(os.environ["ORGN"]))[0] ## label first file

        if nfile==1:
            logging.debug("One file named {0} in {1}. Attempt to copy to {2}".format(firstfile, os.environ["ORGN"], os.environ["DSTN"]))
            print("One file named {0} in {1}. Attempt to copy to {2}".format(firstfile, os.environ["ORGN"], os.environ["DSTN"]))
            #Transfer the file from src path to dest path

            #scp.put(os.path.join(os.environ["orgn"], firstfile),'os.environ["dstn"]')
            os.system("cp " + os.path.join(os.environ["ORGN"], firstfile) + ' ' + os.environ["DSTN"])     
            
            logging.debug("{0} file copied from {1} to {2}".format(firstfile, os.environ["ORGN"], os.environ["DSTN"]))
            print("{0} file copied from {1} to {2}".format(firstfile, os.environ["ORGN"], os.environ["DSTN"]))
            logging.debug("Attempt to remove {0} from {1}".format(firstfile, os.environ["ORGN"]))
            print("Attempt to remove {0} from {1}".format(firstfile, os.environ["ORGN"]))
            os.remove(os.environ["ORGN"] + '/' + firstfile)
            logging.debug("file removed from {0}".format(os.environ["ORGN"]))
            print("file removed from {0}".format(os.environ["ORGN"]))                  
        elif nfile < os.environ['NMAX']:
            logging.debug("Multiple files in {0} ({1} total). Attempt to copy {2} to {3}.".format(os.environ["ORGN"], nfile,
                                                                                                  firstfile, os.environ["DSTN"]))
            #Transfer the file from src path to dest path 
            #scp.put(os.path.join(os.environ["orgn"], firstfile),'os.environ["dstn"]')
            os.system("cp " + os.path.join(os.environ["ORGN"], firstfile) + ' ' + os.environ["DSTN"])     
           
            logging.debug("{0} file copied from {1} to {2}".format(firstfile, os.environ["ORGN"], os.environ["DSTN"]))
            logging.debug("Attempt to remove {0} from {1}".format(firstfile, os.environ["ORGN"]))
            os.remove(os.environ["ORGN"] + '/' + firstfile)

            logging.debug("file removed from {0}. There are {1} files remaining.".format(os.environ["ORGN"],nfile-1))
            #MOVE NEXT FILE? (call this function again?)
        else :
            logging.debug("Greater than {0} files".format(os.environ('NMAX')))
            print("Greater than {0} files".format(os.environ('NMAX')))                          
            #DELETE ALL FILES IN ORIGIN?
    return

move_file()
#Close the connection
#scp.close()
