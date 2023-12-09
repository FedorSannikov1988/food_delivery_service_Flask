from datetime import datetime, \
                     timedelta
from config import UPPER_AGE_YEARS, \
                   LOWER_AGE_YEARS, \
                   TIME_TO_ACTIVATE_ACCOUNT_HOURS, \
                   DURATION_PASSWORD_RECOVERY_LINK_MINUTES


class WorkingWithTimeInsideApp:
    __data_format: str = "%Y-%m-%d"
    __number_days_per_year: int = 365
    __data_and_time_format: str = "%d.%m.%Y %H:%M:%S"

    def checking_user_age(self, date_birth):

        date_birt_str: str = str(date_birth)

        for_lower_bound: timedelta = \
            timedelta(days=
                      self.__number_days_per_year * LOWER_AGE_YEARS)

        for_upper_bound: timedelta = \
            timedelta(days=
                      self.__number_days_per_year * UPPER_AGE_YEARS)

        date_now: datetime = datetime.now()

        lower_bound = \
            date_now - for_lower_bound

        upper_bound = \
            date_now - for_upper_bound

        conversion_date = \
            datetime.strptime(date_birt_str, self.__data_format)

        return upper_bound <= conversion_date <= lower_bound

    def get_data_and_time(self) -> str:
        return datetime.now().strftime(self.__data_and_time_format)

    def checking_date_and_time_registration_user(self,
                                                 date_and_time_registration_user: str) -> bool:

        conversion_date = \
            datetime.strptime(date_and_time_registration_user,
                              self.__data_and_time_format)

        return conversion_date + timedelta(hours=TIME_TO_ACTIVATE_ACCOUNT_HOURS) >= datetime.now()

    def checking_time_password_recovery_request(self,
                                                time_receipt_request: str) -> bool:

        conversion_date = \
            datetime.strptime(time_receipt_request,
                              self.__data_and_time_format)

        return conversion_date + timedelta(minutes=DURATION_PASSWORD_RECOVERY_LINK_MINUTES) >= datetime.now()

