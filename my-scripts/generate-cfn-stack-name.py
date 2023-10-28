"""About program"""
from datetime import datetime
#import sys # sys.exit(0) to exit function
#import pytz # https://pytz.sourceforge.net/#latest-versions
#from prettytable import PrettyTable # 
#import time # https://docs.python.org/3/library/time.html
#from colorama import Fore, Back, Style # https://pypi.org/project/colorama/
#from colorama import init
#init(autoreset=True)

def generate_cfn_tack_name():
    """Function printing python version."""
    stack_name_suffix = input("Enter the stack name suffix (e.g.,'s1' for 'stack1'):") or "s1"
    print("The stack name (suffix) is:", stack_name_suffix)
    date_utc_prefix = datetime.utcnow().strftime('%d-%m-%y')
    print("The date (UTC) (prefix) is:", date_utc_prefix)
    stack_name = date_utc_prefix + "-" + stack_name_suffix
    print("The stack name is:", stack_name)

# Call the function
generate_cfn_tack_name()
