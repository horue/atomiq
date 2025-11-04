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
    def saveUsername(fileName, mode="w", message=""):
        username = System.getUsername().capitalize()
        try:
            f = open(fileName, mode)
            f.write(username)
            if message == "True": 
                print(f"File saved at {fileName}.")
        except Exception as e:
            print(f"Error when executing: {e}")

