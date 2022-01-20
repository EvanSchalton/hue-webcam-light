import subprocess
import time


def count_camera_users():
    """
    Counts the number of processes
    that are using a camera
    """
    return len(
        subprocess.check_output(["lsof -n | grep VDC"], shell=True, text=True)
    )


def watch(wait_seconds, on_function, off_function):
    """
    Checks if a camera attaches to a processes
    Should be started with all cameras off
    """
    base_line = count_camera_users()
    while True:
        if count_camera_users() > base_line:
            on_function()
            # turn_on(bridge, light_names)
        else:
            off_function()
            # turn_off(bridge, light_names)
        time.sleep(wait_seconds)
