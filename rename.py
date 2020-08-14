import glob
import os
import datetime
import sys

cd=r"D:\Test\folder\test2\Test"
for root,dirt,fn in os.walk(cd):
    files=glob.glob(root+"\*")
    files.sort(key=os.path.getmtime)
    #print(files)
    for f in files:
        #if os.path.isfile(f):
        base= os.path.basename(os.path.abspath(f))
        print(base,":",datetime.datetime.fromtimestamp(os.path.getmtime(f)))
        print("------------------------------------")

for root,drname,filename in os.walk(cd):
    #To rename filename
    c=1
    for files in filename:
        files=os.path.join(root,files)    
        base= os.path.basename(os.path.abspath(files))
        #print(base,":",datetime.datetime.fromtimestamp(os.path.getmtime(files)))
                #print(os.path.splitext(base)[0],os.path.splitext(base)[1])
                #fname=os.path.splitext(base)[0]+sys.argv[1]+str(c)
        fname=sys.argv[1]+str(c)
        nname=fname+os.path.splitext(base)[1]
        print(nname)
        nname=os.path.join(root,nname)
        os.rename(files,nname)
        print("-----------------------------------------------")
        c= c+1
    
