from TIPLSB import tiplsb
from TIPLSB import tip_decode
from TIPLSB import read_ring_redundancy
from TIPLSB import read_ring
from PIL import Image

import time
import numpy as np
import random
from datetime import datetime
import hashlib

# start_time = time.time()
# i = tiplsb("img/p.png")
# i.add("BrunoGon", "PLATPRUEBA")
# i.save()
# print("Inicializada la imagen")
# print("--- %s seconds ---" % (time.time() - start_time))
# print(i.init)
# print(i.hash_image)

img = Image.open("img/p.png", 'r').convert('RGB')
width, height = img.size
img_array = np.array(list(img.getdata()))
#
# print("-------------------------------")
#seed_image = hex(int(i.hash_image, 16) + int(str(2), 16))[2:]
aa = read_ring_redundancy(img_array, 1, "145204910812ee5fc75a45a98dc4cd208711003ecfd5c5f8561926714f1f9789", 5, width, height)
for i in aa:
    print(i)
print("....")
print(aa)

#print(read_ring(i.img_array, 3, seed_image, i.width, i.height))
