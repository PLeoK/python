from datetime import datetime, timedelta

ttl = input("Enter TTL in hours: ")

def deletion_time(ttl):
    print("Time now is: ")
    print(datetime.now())
    # Timedelta in minutes...
    #delete_at_time = datetime.now() + timedelta(minutes=int(ttl))
    # Timedelta in hours...
    delete_at_time = datetime.now() + timedelta(hours=int(ttl))
    print("Delete time will be: ")
    print(delete_at_time)
    hh = delete_at_time.hour
    mm = delete_at_time.minute
    yyyy = delete_at_time.year
    month = delete_at_time.month
    dd = delete_at_time.day
    # minutes hours day month day-of-week year
    cron_exp = "cron({} {} {} {} ? {})".format(mm, hh, dd, month, yyyy)
    return cron_exp

print("Starting the program...")

response = deletion_time(ttl)
print("Delete time cron expression is: ")
print(response)
print("Ending program...")
