import json
import os

def ping():
     print("pong")


def readFile(fileDirectoryFromBaseFolder):

    #read the thing
    try:
        with open(fileDirectoryFromBaseFolder, "r") as fileInQuestion:
            fileRead = fileInQuestion.read()

        #first return is success, second is output
        return True, fileRead
    
    #Exception just seemed to be saying vaguely what fucked up
    except Exception as e:
        print(f"something fucked up with the file reading ({e})")
        return False, "ERROR"


def loadText(submittedPath):
    fullTextPath = os.path.join("./teams", submittedPath)

    if os.path.exists(fullTextPath):
        with open(fullTextPath, "r", encoding="utf-8") as f:
            text = f.read()
            return(text)
    else:
        return(None)
        

def loadFileAsJSON(fileDirectoryFromBaseFolder):

    fileReadSuccess, fileOutput = readFile(fileDirectoryFromBaseFolder)
    #checks if readFile threw an error and only does the thing if it didn't
    if fileReadSuccess:

        loadedFileAsJSON = json.loads(fileOutput)
        #load the text we just read and send it back as a dict
        return loadedFileAsJSON
        

    elif not fileReadSuccess:
            print(f"couldn't read file {fileDirectoryFromBaseFolder}")




def grabValueFromJSON(fileDirectoryFromBaseFolder, dictValue):

    fileReadSuccess, fileOutput = readFile(fileDirectoryFromBaseFolder)
    if fileReadSuccess:

        try:
            loadedFileAsJSON = json.loads(fileOutput)
            return loadedFileAsJSON[dictValue]
        
        except:
            print("dunno what you sent but it wasn't a dictValue")
            return None
        
        
    elif not fileReadSuccess:
            print(f"couldn't read file {fileDirectoryFromBaseFolder}")




def dumpJSON(fileDirectoryFromBaseFolder):

    fileReadSuccess, fileOutput = readFile(fileDirectoryFromBaseFolder)
    if fileReadSuccess:

        loadedFileAsJSON = json.loads(fileOutput)
        return json.dumps(loadedFileAsJSON)     

    elif not fileReadSuccess:
            print(f"couldn't read file {fileDirectoryFromBaseFolder}")