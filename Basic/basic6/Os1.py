import os

# path to list ti the module
rst = os.listdir('/')
for st in rst:

    print st

    if os.path.isdir(st) == True:
        print 'Dir : ', st
    elif os.path.isfile(st) == True:
        print 'File : ', st