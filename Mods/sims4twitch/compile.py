from Utilities import compile_module
from settings import *

root = os.path.dirname(os.path.realpath('__file__'))
compile_module(root, mods_folder)
