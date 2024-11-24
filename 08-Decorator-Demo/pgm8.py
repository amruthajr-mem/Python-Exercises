from functools import wraps
import time
def time_this(func):
    '''
    this function wraps
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
        this function is what really wraps
        '''
        print(f'---> Running {func.__name__}')
        start = time.time()
        func(*args, **kwargs)
        print(f'---> Completed {func.__name__} in {time.time() - start}')
    return wrapper
@time_this
def sleeper_func(duration):
    '''
    this function simply sleeps
    '''
    print(f'sleeping for {duration}')
    time.sleep(duration)

print(sleeper_func.__doc__)
sleeper_func(2)