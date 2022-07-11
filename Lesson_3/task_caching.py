import time
from functools import wraps


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        result_time = round(time.time() - start_time, 2)
        print(f'Время выполнения функции {func.__name__}: {result_time} с.')
        return result

    return wrapper


def cache_args(func):
    cache_dict = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return wrapper


@time_check
@cache_args
def multiplier(number: int):
    time.sleep(1)
    return number * 2


if __name__ == "__main__":
    print(multiplier(5))
    print(multiplier(5))
    print(multiplier(2000))
    print(multiplier(2000))
