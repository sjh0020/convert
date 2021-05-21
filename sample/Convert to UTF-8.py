import os;
import sys;
sys.stdout = console
 # from Npp import notepad++ # import it first!
 # print "Convert to UTF-8"
filePathSrc="D:\\game" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
     for fn in files: 
          if fn[-4:] == '.xml': # Specify type of the files
              notepad.open(root + "\\" + fn)      
              notepad.runMenuCommand("Encoding", "Convert to UTF-8")
              notepad.save()
              notepad.close()
			  
print "Convert to UTF-8 Finish"