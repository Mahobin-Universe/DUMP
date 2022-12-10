import os, sys
try:
    __import__("BadBoy").login()
except Exception as e:
    exit(str(e))