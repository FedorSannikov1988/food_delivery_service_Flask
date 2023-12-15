"""
This package imports all modules and
packages of the application to run.
"""
from .views import app
from .commands import app
from .redirection import app
from .db_api import path_for_meal, \
                    loading_fixtures


