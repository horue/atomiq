from interpreter.modules.user import *
from interpreter.modules.system import *
from interpreter.modules.ollama import *


STD = {
    "User": {
        "show": User.show,
        "showSl": User.showSl,
        "clear": User.clear
    },
    "System":{
        "pause": System.pause,
        "saveUsername": System.saveUsername
    },
    "Ollama":{
        "generate": Ollama.generate,
        "chat": Ollama.chat
    }
}