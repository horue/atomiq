import os

class System():
    @staticmethod
    def pause():
        print("Press any key to continue...")
        input()

    @staticmethod
    def getUsername():
        username = os.getlogin()
        return username
    
    @staticmethod
    def saveUsername(fileName, mode):
        username = System.getUsername().capitalize()
        f = open(fileName, mode)
        f.write(username)

