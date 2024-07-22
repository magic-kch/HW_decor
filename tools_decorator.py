from functools import wraps
from datetime import datetime


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open("main.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()}: {old_function.__name__}, {args}, {kwargs}, {result}\n")
        return result

    return new_function


def logger_with_param(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, "a", encoding="utf-8") as log_file:
                log_file.write(f"{datetime.now()}: {old_function.__name__}, {args}, {kwargs}, {result}\n")
            return result
        return new_function

    return __logger
