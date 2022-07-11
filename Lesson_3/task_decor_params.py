from functools import wraps
import time


def repeat_decor(call_count, start_sleep_time, factor, border_sleep_time):
    """
    :param call_count: число, описывающее кол-во раз запуска функций;
    :param start_sleep_time: начальное время повтора;
    :param factor: во сколько раз нужно увеличить время ожидания;
    :param border_sleep_time: граничное время ожидания.
    """

    def main_decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Количество запусков = {call_count}')
            print('Начало работы')
            sleep_time = start_sleep_time
            for i in range(call_count):
                value = func(*args, **kwargs)
                if sleep_time < border_sleep_time:
                    sleep_time *= 2 ** factor
                    if sleep_time >= border_sleep_time:
                        sleep_time = border_sleep_time
                print(f'Запуск номер {i + 1}. Ожидание:'
                      f' {sleep_time} секунд. Результат декорируемой функций = {value}')
                time.sleep(sleep_time)
            print('Конец работы')

        return wrapper

    return main_decor


@repeat_decor(3, 1, 2, 30)
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    multiplier(5)
    multiplier(2000)
