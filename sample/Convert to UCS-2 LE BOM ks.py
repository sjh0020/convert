import os;
import sys;
sys.stdout = console
 # from Npp import notepad++ # import it first!
 # print "Convert to UCS-2 LE BOM"
filePathSrc="D:\\game\\1" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
     for fn in files: 
          if fn[-3:] == '.ks': # Specify type of the files
              notepad.open(root + "\\" + fn)      
              notepad.runMenuCommand("Encoding", "Convert to UCS-2 LE BOM")
              notepad.save()
              notepad.close()
			  
print "Convert to UCS-2 LE BOM Finish"