from parser.tokenizer import AtomiqParser
from interpreter.interpreter import AtomiqInterpreter
import time
import os
import sys



def runAtCode(path: str):
    startTime = time.perf_counter()

    codePath = r'examples\exemplo2.at'
    code = open(codePath).read()
    tree = AtomiqParser.build(code)
    interpreter = AtomiqInterpreter()

    os.system('cls')

    print(f"Atomiq - {codePath}\n")

    final = interpreter.transform(tree)

    endTime = time.perf_counter()
    totalTime = endTime - startTime
    print(f'\nExecuted in: {totalTime:.2f} seconds.')

    return







if __name__ == "__main__":
    codePath = sys.argv[1]
    runAtCode(codePath)

