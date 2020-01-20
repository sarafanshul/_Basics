# from tqdm import tqdm
# # for i in tqdm(range(100)):
# for i in tqdm(range(100) , ascii = True):
# 	time.sleep(0.1+(i*10)//10000)

from tqdm import trange
from time import sleep
t = trange(100, desc='Bar desc', leave=True)
for i in t:
    t.set_description("Bar desc (file %i)" % i)
    t.refresh()  # to show immediately the update
    sleep(0.01)