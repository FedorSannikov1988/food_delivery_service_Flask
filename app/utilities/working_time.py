from datetime import datetime, \
                     timedelta
from config import UPPER_AGE_YEARS, \
                   LOWER_AGE_YEARS, \
                   TIME_TO_ACTIVATE_ACCOUNT_HOURS


DATE_FORMAT: str = "%Y-%m-%d"
NUMBER_DAYS_PER_YEAR: int = 365
DATE_AND_TIME_FORMAT: str = "%d.%m.%Y %H:%M:%S"


def checking_user_age(date_birth: datetime.date) -> bool:
    date_birt_str: str = str(date_birth)

    for_lower_bound: timedelta = \
        timedelta(days=
                  NUMBER_DAYS_PER_YEAR * LOWER_AGE_YEARS)

    for_upper_bound: timedelta = \
        timedelta(days=
                  NUMBER_DAYS_PER_YEAR * UPPER_AGE_YEARS)

    date_now: datetime = datetime.now()

    lower_bound = \
        date_now - for_lower_bound

    upper_bound = \
        date_now - for_upper_bound

    conversion_date = \
        datetime.strptime(date_birt_str, DATE_FORMAT)

    return upper_bound <= conversion_date <= lower_bound


def get_data_and_time() -> str:
    return datetime.now().strftime(DATE_AND_TIME_FORMAT)


def checking_date_and_time_registration_user(date_and_time_registration_user: str) -> bool:

    conversion_date = \
        datetime.strptime(date_and_time_registration_user,
                          DATE_AND_TIME_FORMAT)

    return conversion_date + timedelta(hours=TIME_TO_ACTIVATE_ACCOUNT_HOURS) >= datetime.now()
