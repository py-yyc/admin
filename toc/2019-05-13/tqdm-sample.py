import time
from tqdm import tqdm

subjects = ('Python', 'Coding', 'Tips')

for subject in tqdm(subjects):
  time.sleep(0.25)
