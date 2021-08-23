import os;
import sys;
sys.stdout = console
 # from Npp import notepad++ # import it first!
filePathSrc="D:\\test" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
     for fn in files: 
          if fn[-3:] == '.ks': # Specify type of the files
              notepad.open(root + "\\" + fn)      
              notepad.runMenuCommand("Encoding", "Convert to UTF-16 LE BOM")
              notepad.save()
              notepad.close()
print "Convert to UTF-16 LE BOM Finish"
