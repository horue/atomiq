import os

class User():
    ## @User.show:string:
    @staticmethod
    def show(*args):
        if len(args) > 1:
            raise Exception("Execution Error: @User.show can only use one argument.")
        if len(args) < 1:
            raise Exception("Execution Error: @User.show can not be empty.")
        if len(args) == 1:
            print(args[0])

    @staticmethod
    def clear():
        os.system('cls')
