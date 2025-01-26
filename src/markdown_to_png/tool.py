import time, math


def progress_bar(bar_time: int, duration: float):
    """ Display a progress bar for the estimated duration

        :param bar_time: the length of the progress bar (number of characters)
        :param duration: the estimated time(in seconds) for the process to complete
    """

    steps = 100 # total steps for the progress bar
    step_duration = duration / steps    # time for each step

    for p in range(steps + 1):
        chars = math.ceil(p * (bar_time / steps))
        print('▮' * chars + '▯' * (bar_time - chars), f'{p}%', end='\r')
        time.sleep(step_duration)

    print('▮' * bar_time + ' 100%')
