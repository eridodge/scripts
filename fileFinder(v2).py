import os
from fnmatch import fnmatch
import time
from datetime import datetime

def removeFile(fileNum):
    with open("curLogFile.txt",'r') as inputFile:
        files = inputFile.readlines()
        line = files[fileNum-1]
        line = line.encode().expandtabs(1)
        line = line.strip(b"\n")
        line = line.partition(b" ::: ")[0].partition(b": ")[2].partition(b": ")[2].decode()

        os.remove(line)
        print("File at path: '{}' was successfully removed".format(line))

def fileSearch():
    # Drive/directory/folder File Type locator/logger
    # Eric Dodge && Mitch Pemberton
    # CSO
    # 2/18/2017

    count = 0
    numFiles = 0

    if count == 0: # setup a while loop to repeat if wanted


        # Open a file
        root = 'C:\\'    # Base setup will be this Directory
        pattern = "*.exe" # Base file type search will be .exe

        fileSelection = input("\nDo you want to write the output to a file? (y/n)[y]: ")
        if fileSelection == "": # If no option given, use default of 'y'
            fileSelection = "y"
        if fileSelection == "y":
            file = open("curLogFile.txt",'w')


        driveSelection=input("Enter the drive, directory, or folder [{}]: ".format(root)) # Enter the new root drive
        if driveSelection != "": # If no path given, use default
            root = driveSelection


        patternSelection = input("Please enter the file type you want to search for [{}]: ".format(pattern)) # set the file type
        if patternSelection != "": # If no pattern give, use default
            pattern = patternSelection


        print("========Starting pattern search for '{}' in directory '{}'========\n".format(pattern, root))

        t1 = datetime.now()
        # searches from the root on down through all subdirectories
        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):  # Search for the set pattern and print out/write the ones it finds\
                    fullPath = os.path.join(path,name)
                    numFiles += 1

                    try:
                        modTimeStr = time.strftime("%D %H:%M:%S", time.localtime(os.path.getmtime(fullPath)))
                        #modTimeStr = datetime.now().strftime("%D %H:%M:%S")
                        # modTimeStr = time.strftime("%D %r", time.localtime(os.path.getmtime(fullPath)))
                    except PermissionError as e:
                        modTimeStr = "<PermissionError>"

                    fileDataStr = "{}:\t{}:\t{} ::: {}".format(numFiles, modTimeStr, fullPath, name)

                    print(fileDataStr)
                    #file.write(time.strftime("%c: ")+(os.path.join(path, name)))
                    file.write(fileDataStr)
                    file.write('\n')



        file.write("End of this sessions searches/logs"+'\n')


        t2 = datetime.now()
        print("Time to Completion: {}\n".format((t2-t1).total_seconds()))

        file.close()
        file = open("curLogFile.txt",'r')

        with open("FullLogFile.txt",'a') as fullLog:
            sepStr = """====================Scan Performed at: {}====================\n""".format(datetime.now().strftime("%D %H:%M:%S"))
            fullLog.write(sepStr)
            fullLog.write("Scanned Path: {}\n".format(path))
            fullLog.write("Pattern: {}\n\n".format(pattern))
            fullLog.write(file.read())
            file.close()




        #repeat = input("Would you like to enter another drive or directory? (y/n)[y]: ")  # setup exit on loop or repeat
        repeat = input("Would you like to remove a File or Directory? (y/n)[y]: ")  # setup exit on loop or repeat
        while repeat == 'y':
            index = int(input("Enter the ID of the file to be removed: "))
            removeFile(index)
            repeat = input("Would you like to remove another File or Directory? (y/n)[y]: ")  # setup exit on loop or repeat





# *************************************
# Calling out function for self testing


fileSearch() # remove if importing
#removeFile(2)