from termcolor import colored
import sys

def error(msg,prefix=True):
	txt = msg if prefix==False else "ERROR: "+msg
	print(colored(txt,"white","on_red"))
def warning(msg,prefix=True):
	txt = msg if prefix==False else "WARNING: "+msg
	print(colored(txt,"red",attrs=['bold']))

def info(msg,prefix=True):
	txt = msg if prefix==False else "INFO: "+msg
	print(colored(txt,"blue",attrs=[]))

def critical(msg):
	print(colored("CRITICAL ERROR: ","white","on_red",attrs=['bold',]),end="")
	print(colored(msg,"white","on_red",attrs=['bold',]))

	sys.exit()
