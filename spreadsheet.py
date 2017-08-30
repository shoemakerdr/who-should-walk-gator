
from datetime import datetime
from pendulum import timezone
import gspread
from oauth2client.service_account import ServiceAccountCredentials

AccountCred = ServiceAccountCredentials
chicago = timezone('America/Chicago')
now = chicago.convert(datetime.now())
today = now.today


def get_schedule():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = AccountCred.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Who Should Walk Gator?').sheet1
    schedule = sheet.get_all_records()
    return schedule


def get_data():
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
    hour = now.hour
    day = days[today_or_tomorrow(hour, today().weekday())]
    time_index = get_index_by_hour(hour)
    walker = schedule[time_index][day]
    data = {
            "walker": walker,
            "day": day,
            "time": "morning" if time_index == 0 else "afternoon"
            }
    return data


def today_or_tomorrow(hour, day_index):
    # if before 8pm, return today index
    if hour <= 19:
        return day_index
    # else return tomorrow index
    return (day_index + 8) % 7


def get_index_by_hour(hour):
    # after 8pm and before 11am return 0 morning index
    if hour < 11 or hour > 19:
        return 0
    # between 11am and 8pm return 1 afternoon index
    return 1
