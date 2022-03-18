from datetime import date


# If you'd like to use this yourself, replace these variables:
# first_xp is the first logged amount of total xp you have
# first_date is the date of that first logged xp amount

def main():
    first_xp = 22098000
    first_date = date(2022, 2, 16)

    xp_to_50 = 176000000
    days_since = date.today() - first_date
    print('First xp entry date: ', first_date, '\tXP: ', "{:,}".format(first_xp))
    print('Today\'s date: ', date.today())
    today_xp = input('Enter current XP: ')
    xp_per_day = (int(today_xp) - first_xp) / days_since.days
    print('Average XP per day: ' + "{:,}".format(round(xp_per_day)))
    print('At this pace, level 50 will occur in ' + str(round((xp_to_50 - int(today_xp)) / xp_per_day)) + ' days.')


if __name__ == '__main__':
    main()
