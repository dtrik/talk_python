import datetime

def print_header():
    print('---------------------------------------')
    print('       GET DAYS TO BIRTHDAY APP')
    print('---------------------------------------')
    print()


def get_user_birthday():
    print("ENTER YOUR BIRTHDAY")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))
    bday = datetime.date(year, month, day)
    return bday


def get_difference(original_date, target_date):
    date_this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    date_diff = date_this_year - target_date
    return date_diff.days


def print_date_info(date):
    if date > 0:
        print("There are {} days for your next birthday".format(date))
    elif date < 0:
        print("It has been {} days since your last birthday".format(-date))
    else:
        print("Happy Birthday!!!") 


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    date_diff = get_difference(bday, today)
    print("You were born on {}".format(bday))
    print_date_info(date_diff)


main()