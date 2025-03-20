# Ez a script, akkor fut le, ha egy programba beimportáljuk ezt a könyvtárat
print("Sikeresen importáltad ezt: MyPackage")

from .functions import * # functions scriptből importáljunk be mindent
from .data import *