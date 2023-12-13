from .models import Meal, \
                    CategoriesMeal
from .loading_fixtures import path_for_meal, \
                              loading_fixtures, \
                              path_for_categories_meal
from .requests import get_meal, \
                      add_user_photo, \
                      change_password, \
                      delete_user_photo, \
                      add_user_in_database, \
                      change_personal_data, \
                      searching_user_account, \
                      get_all_categories_meal, \
                      search_for_meal_by_title, \
                      change_default_shipping_address, \
                      search_for_categories_meal_by_name, \
                      searching_and_activating_user_account, \
                      searching_user_account_and_setting_new_password
