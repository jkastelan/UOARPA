def move_file():
    Popen("gphoto2 -f -p")
    nfile = len(os.listdir("."))
    if nfile>0:  ## are there any files to move
        firstfile = sorted(os.listdir("."))[0] ## label first file
        if nfile==1:
            log("One file named {0} in {1}. Attempt to copy to {2}".format(firstfile, $ORGN, $DSTN)
            shutil.copy2($ORGN/firstfile, $DSTN/firstfile)
            log("{0} file copied from {1} to {2}".format(filename, $ORGN, $DSTN))
            log("Attempt to remove {0} from {1}".format(filename, $ORGN))
            os.remove($ORGN/firstfile)
            log("file removed from {0}".format($ORGN))
        elif 1 < nfile < $NMAX:
            log("Multiple files in {0} ({1} total). Attempt to copy {2} to {3}.".format($ORGN, nfile, firstfile, $DSTN)
            shutil.copy2($ORGN/firstfile, $DSTN/firstfile)
            log("{0} file copied from {1} to {2}".format(filename, $ORGN, $DSTN))
            log("Attempt to remove {0} from {1}".format(filename, $ORGN)
            os.remove($ORGN/firstfile)
            log("file removed from {0}. There are {1} files remaining.".format($ORGN,nfile-1)
            #MOVE NEXT FILE? (call this function again?)
        else 
            log("Greater than {} files".format($NMAX))
            #DELETE ALL FILES IN ORIGIN?
