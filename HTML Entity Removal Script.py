#HTML Space Removal Script
#Author Jimmy M Bowden Jr.
#Purpose of this scrip is to remove HTML space entities like "&nbsp;" and any "double" spaces
#This is being created to remove the need to use notepad++ to remove spaces and streamline the process

from tkinter import Tk

#---------------------Variables------------------------
#strings
userInputPromptString = "Hello User, please enter the text that you wish to have processed and hit Enter to continue. "
altString1 = ""
altString2 = ""

#ints
HTMLNBSpaceCount = 0
doubleSpaceCount = 0

#testing Vars
testString1 = "Test  test  test &nbsp;  test test"
testString2 = "test&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test"

#---------------------Function--------------------------

#HTMLNBSpaceReplace(inputString)
#This is used to parse a string for any &nbsp; and replace it with a space
#Returns a tuple with a string and count
def HTMLNBSpaceReplace(inputString):
    print(inputString)
    HTMLNBSpaceCount = inputString.count("&nbsp;")
    altString1 = inputString.replace("&nbsp;", " ")
    HTMLNBSpaceTuple = (HTMLNBSpaceCount, altString1)
    return HTMLNBSpaceTuple

#doubleSpaceReplace(inputString)
#This is used to parse a string for double spaces and convert them into single spaces
#Recurses until all strings are single strings
def doubleSpaceReplace(inputString):
    doubleSpaceCount = inputString.count("  ")
    if doubleSpaceCount == 0:
        altString2 = inputString
        doubleSpaceTuple = (doubleSpaceCount, altString2)
        return doubleSpaceTuple

    else:
        altString = inputString.replace("  ", " ")
        altString2 = altString.replace("  ", " ")
        return doubleSpaceReplace(altString2)


#copyToClipboard(inputString)
#This is used to copy the final string into the clipboard
def copyToClipboard(inputString):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(inputString)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
    return

#startScript()
#this begins the script
#Intro to user and ask for string
#ask for string
def startScript():
    print(userInputPromptString)
    inputString = input()

#parse string for &nbsp; and replace with a space
    HTMLNBSpaceTuple = HTMLNBSpaceReplace(inputString)
    altString1 = HTMLNBSpaceTuple[1]
    HTMLNBSpaceCount = HTMLNBSpaceTuple[0]


#parse new version of string for double space
    doubleSpaceTuple = doubleSpaceReplace(altString1)
    altString2 = doubleSpaceTuple[1]
    doubleSpaceCount = doubleSpaceTuple[0]


#copy final string into clipboard
    copyToClipboard(altString2)
    print("There were " + str(HTMLNBSpaceCount) + " &nbsp; in the original string.")
    print("There were " + str(doubleSpaceCount) + " double spaces in the original string.")
    print("The result is now in your clipboard. You can now paste it.")
    startScript()


#restartScript()
#this restarts the script and allows the window to stay open

    

#---------------------Main Process---------------------
startScript()



