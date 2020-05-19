# This file contains different progress bar tests.
# option 1 : https://github.com/tqdm/tqdm, https://pypi.org/project/tqdm/
# to use this, pip install progress
from tqdm import tqdm
import time


def progress_check_tqdm(custom_range):
    for i in tqdm(range(custom_range)):
        time.sleep(1)


progress_check_tqdm(25)

