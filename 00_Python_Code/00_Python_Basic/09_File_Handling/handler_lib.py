
def Open_File (File_Path , Mode):
    try :
        file_handler = open(File_Path ,Mode )
        print("File Opend sccessfuly ")
        return  file_handler
    except Error :
        print("Couldn't Opened File ")
        return None


def Close_File (File_Path):
    try:
        File_Path.close()
        print("File Closed sccessfuly ")
    except Error:
        print("Couldn't Close File ")
    except AttributeError :
        print("Couldn't Close None File ")

