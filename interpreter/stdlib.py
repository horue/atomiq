from interpreter.modules.user import *
from interpreter.modules.system import *


STD = {
    "User": {
        "show": User.show,
        "clear": User.clear
    },
    "System":{
        "pause": System.pause
    }
}