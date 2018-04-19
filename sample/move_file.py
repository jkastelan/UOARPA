from paramiko import SSHClient
from scp import SCPClient
import os
import logging

# Ensure you have run key-based authentication setup    
ssh = SSHClient()
ssh.load_systen_host_keys()
with SCPClient(ssh.get_transport()) as scp:


def move_file():
    nfile = len(os.listdir("."))

    if nfile>0:  ## are there any files to move
        firstfile = sorted(os.listdir("."))[0] ## label first file
        if nfile==1:
            logging.debug("One file named {0} in {1}. Attempt to copy to {2}".format(firstfile, os.environ["orgn"], os.environ["dstn"])
            #Transfer the file from src path to dest path 
            scp.put('os.environ["orgn"]','os.environ["dstn"]')     
            shutil.copy2('os.environ["orgn"]/firstfile', 'os.environ["dstn"]/firstfile')
            logging.debug("{0} file copied from {1} to {2}".format(filename, os.environ["orgn"], os.environ["dstn"]))
            logging.debug("Attempt to remove {0} from {1}".format(filename, os.environ["orgn"]))
            os.remove('os.environ["orgn"]/firstfile')
            logging.debug("file removed from {0}".format(os.environ["orgn"]))
        elif 1 < nfile < os.environ('NMAX'):
            logging.debug("Multiple files in {0} ({1} total). Attempt to copy {2} to {3}.".format(os.environ["orgn"], nfile, firstfile, os.environ["dstn"])
            #Transfer the file from src path to dest path 
            scp.put('os.environ["orgn"]','os.environ["dstn"]')
            logging.debug("{0} file copied from {1} to {2}".format(filename, os.environ["orgn"], os.environ["dstn"]))
            logging.debug("Attempt to remove {0} from {1}".format(filename, os.environ["orgn"])
            os.remove('os.environ["orgn"]/firstfile')
            logging.debug("file removed from {0}. There are {1} files remaining.".format(os.environ["orgn"],nfile-1)
            #MOVE NEXT FILE? (call this function again?)
        else 
            logging.debug("Greater than {0} files".format(os.environ('NMAX')))
            #DELETE ALL FILES IN ORIGIN?
    return

#Close the connection
scp.close()
