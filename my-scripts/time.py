"""About program"""
from datetime import datetime, timezone
#import sys # sys.exit(0) to exit function
import pytz # https://pytz.sourceforge.net/#latest-versions
from prettytable import PrettyTable # 
#import time # https://docs.python.org/3/library/time.html
from colorama import Fore, Back, Style # https://pypi.org/project/colorama/
from colorama import init
init(autoreset=True)

def print_timestamp():
    """About function"""
    # Define format of datetime
    time_format = "%d-%m-%Y %H:%M:%S %Z%z"
    # Store local timezone time value
    local = datetime.now()

    #print("Local:", local.strftime(time_format))
    #print(Fore.YELLOW + "Local:", local.strftime(time_format))

    tz_SIN = pytz.timezone('Asia/Singapore')
    datetime_SIN = datetime.now(tz_SIN)

    tz_KOLKATA = pytz.timezone('Asia/Kolkata')
    datetime_KOLKATA = datetime.now(tz_KOLKATA)

    tz_UTC = pytz.timezone('UTC')
    datetime_UTC = datetime.now(tz_UTC)
    #print("UTC:", datetime_UTC.strftime(time_format))
    #print(Fore.GREEN + "UTC:", datetime_UTC.strftime(time_format))

    tz_LHR = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_LHR)
    #print(Fore.BLACK + "London:", datetime_London.strftime(time_format))

    tz_EASTERN = pytz.timezone('US/Eastern')
    datetime_EASTERN = datetime.now(tz_EASTERN)
    #print(Fore.RED + "NY:", datetime_EASTERN.strftime(time_format))

    tz_PACIFIC = pytz.timezone('US/Pacific')
    datetime_PACIFIC = datetime.now(tz_PACIFIC)

    # Creating instance of PrettyTable class
    my_table = PrettyTable(["Timezone", "Date and Time"])

    # Adding table rows to a list that we want to tabulate
    my_table.add_row([Fore.WHITE + "Local:", local.strftime(time_format) + Style.RESET_ALL])
    my_table.add_row([Fore.YELLOW + "SIN:", datetime_SIN.strftime(time_format) + Style.RESET_ALL])
    my_table.add_row([Fore.RED + "IST:", datetime_KOLKATA.strftime(time_format) + Style.RESET_ALL])
    my_table.add_row([Fore.GREEN + "UTC:", datetime_UTC.strftime(time_format) + Style.RESET_ALL])
    my_table.add_row([Fore.BLACK + "LHR:", datetime_London.strftime(time_format) + Style.RESET_ALL])
    my_table.add_row([Fore.MAGENTA + "US/Eastern:", datetime_EASTERN.strftime(time_format) + Style.RESET_ALL])
    my_table.add_row([Fore.BLUE + "US/Pacific:", datetime_PACIFIC.strftime(time_format) + Style.RESET_ALL])

    # Print table
    print(my_table)

def time_delta():
    """About function"""   
    # Define format
    input_time_format = "%d-%m-%Y %H:%M:%S"

    # Ask user for input in string format
    # Add error handling
    # https://linuxhint.com/python-keyboardinterrupt/
    # https://www.programiz.com/python-programming/exception-handling
    # https://www.freecodecamp.org/news/python-print-exception-how-to-try-except-print-an-error/

    try:
        print("")
        print("Please enter UTC timestamp (format %d-%m-%Y %H:%M:%S)")
        print("Example UTC input: 19-6-2023 12:00:00. Or Ctrl + C to exit):")
        str_d1 = input()
        # Test input
        #str_d1 = "19-6-2023 12:00:00"

        # Generate time now in UTC
        object_d2 = datetime.now(timezone.utc)

        # See type
        #print(str_d1)
        #print(type(str_d1))

        # See type
        #print(object_d2)
        #print(type(object_d2))

        #Convert issue start time to all other timeoznes and datetime object.
        # https://note.nkmk.me/en/python-datetime-timedelta-measure-time/
        # https://pynative.com/python-difference-between-two-dates/
        # The strptime() method creates a datetime object from the given string.
        # Note: You cannot create datetime object from every string.
        # The string needs to be in a certain format.
        # https://www.programiz.com/python-programming/datetime/strptime
        object_d1 = datetime.strptime(str_d1, input_time_format)
        #print(type(object_d2))

        # The strftime() method converts date, time and datetime objects
        # to its equivalent string (with the help of examples)
        # https://www.programiz.com/python-programming/datetime/strftime
        #print("")
        #print("Current time (UTC):", object_d2.strftime(input_time_format))
        #print("Start time (UTC):", object_d1.strftime(input_time_format))


        # Subtract offset-naive and offset-aware datetimes
        # https://tiny.amazon.com/vmynl5ps/itsotypecant
        delta = object_d2 - object_d1.replace(tzinfo=timezone.utc)

        # Print delta
        #print(Fore.LIGHTCYAN_EX + "Time since issue started:", delta)

        # Creating instance of PrettyTable class
        my_table_2 = PrettyTable(["Time", "Delta"])

        # Adding table rows to a list that we want to tabulate
        my_table_2.add_row(["Current time (UTC):", object_d2.strftime(input_time_format)])
        my_table_2.add_row(["Start time (UTC):", object_d1.strftime(input_time_format)])
        my_table_2.add_row([Fore.LIGHTCYAN_EX + "Time since issue started:", str(delta) + Style.RESET_ALL])
        # Print table
        print(my_table_2)
    except KeyboardInterrupt as error:
        print("")
        print(Fore.RED + "An exception occurred:", type(error).__name__ + Style.RESET_ALL)
        print("Exiting program. Bye!")
        #sys.exit(0)
    except ValueError as error:
        print("")
        print(Fore.RED + "Ups! Incorrect format.", type(error).__name__  + Style.RESET_ALL)
        print("Run me again. Bye!")
        #sys.exit(0)
    # else:
    #     print('Ugh! Unknown error!')
    #     print("Exiting program. Bye!")
    #     sys.exit(0)

print_timestamp()
#print(pytz.all_timezones)

time_delta()
