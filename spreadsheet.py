
from datetime import date
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

AccountCred = ServiceAccountCredentials
today = date.today
now = datetime.now


def get_schedule():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = AccountCred.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Who Should Walk Gator?').sheet1
    schedule = sheet.get_all_records()
    return schedule


def get_walker():
    schedule = get_schedule()
    days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
    ]
    day = days[today().weekday()]
    hour = now().hour
    time_index = get_index_by_hour(hour)
    walker = schedule[time_index][day]
    return walker


def get_index_by_hour(hour):
    # before 11 am return 0 morning index
    if hour < 11 or hour > 19:
        return 0
    # before 8pm return 1 afternoon index
    return 1

print(get_walker(), 'should walk Gator next.')
