#!/usr/bin/env python3
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
class Folder:
    def __init__(self, name, parent = None):
        self.name = name
        self.children = []
        self.files = []
        self.parent = parent
        self.lastSize = None
    def addFile(self, fileObj):
        self.files.append(fileObj)
    def addFolder(self, folder):
        self.children.append(folder)
    def getFolder(self, name):
        for folder in self.children:
            if folder.name == name:
                return folder
    ### Recursion
    def size(self):
        if self.lastSize:
            return self.lastSize
        fileSize = sum([x.size for x in self.files])
        folderSize = 0
        if len(self.children) > 0:
            for child in self.children:
                folderSize += child.size()
            self.lastSize = fileSize + folderSize
            return fileSize + folderSize
        else:
            self.lastSize = fileSize
            return fileSize
    def walk(self):
        allDirs = []
        allDirs.append(self)
        for child in self.children:
            allDirs += child.walk()
        return allDirs
class Interpreter:
    def __init__(self):
        self.activeFolder = None
        self.root = None
    def splitDataIntoCommandResp(self, data):
        i = 0
        outCommands = []
        while i < len(data):
            line = data[i]
            # command
            if line[0] == '$':
                commands = line.split(' ')[1:]
                command = commands[0]
                if command == 'cd':
                    target = commands[1]
                    outCommands.append([command, target])
                    i += 1
                else:
                    #ls get next lines until $
                    i += 1
                    nextLine = data[i]
                    outStr = []
                    while nextLine[0] != '$':
                        outStr += [nextLine]
                        i += 1
                        if i >= len(data):
                            break
                        nextLine = data[i]
                    outCommands.append(['ls', outStr])
        return outCommands

class fsEmulator:
    def __init__(self):
        self.root = None
        self.activeFolder = None
    def changeDirectory(self, target):
        #if no root exists create root
        if self.activeFolder == None:
            self.root = Folder(target)
            self.activeFolder = self.root
            return
        #if .. go back in file structure
        if target == '..':
            parent = self.activeFolder.parent
            self.activeFolder = parent
            return
        # otherwise change directory
        self.activeFolder = self.activeFolder.getFolder(target)
    def updateDirFromLs(self, dirs):
        for item in dirs:
            size, name = item.split(' ')
            if size == 'dir':
                self.activeFolder.addFolder(Folder(name, self.activeFolder))
            else:
                self.activeFolder.addFile(File(name, int(size)))
    def getFilesUnderSize(self, fileSize):
        # can optimize by getting size while walking or not even walking
        outFolders = []
        totSize = 0
        allFolders = self.root.walk()
        for folder in allFolders:
            size = folder.size()
            if size < fileSize:
                outFolders.append(folder)
                totSize += size
        print('files found:', len(outFolders))
        return totSize

            
with open('../data/day7.txt') as f:
    data = f.read()

lines = data.strip().split('\n')
I = Interpreter()
commands = I.splitDataIntoCommandResp(lines)
fs = fsEmulator()

for commandTup in commands:
    command, target = commandTup
    if command == 'cd':
        fs.changeDirectory(target)
    else:
        fs.updateDirFromLs(target)
solution1 = fs.getFilesUnderSize(100000)
print('Solution 1', solution1)
#solution 2 total disk space = 70000000 need 30000000 free find smallest dir to delete

#definitely can optimize, first thing we do is call root walk which looks at every folder, then we call size on each folder even though root calls size on every folder in the first iteration
sizeAvaiable = 70000000 - fs.root.size()
sizeNeeded = 30000000 - sizeAvaiable
print('Size available:', sizeAvaiable)
print('Size needed:', sizeNeeded)
allFolders = fs.root.walk()
allSizes = [x.size() for x in allFolders]
allSizes.sort()
for i, size in enumerate(allSizes):
    if size >= sizeNeeded:
        print('Smallest folder', allFolders[i].name)
        print('Size:', size)
        break
