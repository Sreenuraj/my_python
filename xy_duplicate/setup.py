import sys
from cx_Freeze import setup, Executable

setup( name = "Find XY Duplicate", version = "1.0", description = "Duplicate in JSON response", executables = [Executable("xy_findduplicate.py", base = "Console")])