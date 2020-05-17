# This file contains different progress bar tests.
# option 1 : https://github.com/tqdm/tqdm
#option 2 : https://pypi.org/project/progress/ --> lot more options.
  #to use this, pip install progress
from tqdm import tqdm
from progress.bar import Bar
import time


def progress_check_tqdm(custom_range):
  for i in tqdm(range(custom_range)):
    time.sleep(1)

#from: https://pypi.org/project/progress/
def progress_check_pypiprogress(custom_range):
  bar = Bar('Processing', max=custom_range)
  for i in range(custom_range):
    # Do somework
    time.sleep(1)
    bar.next()
  bar.finish()

#progress_check_tqdm(25)
progress_check_pypiprogress(25)

